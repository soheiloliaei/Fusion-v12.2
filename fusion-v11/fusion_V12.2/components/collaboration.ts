"""
Real - time collaboration system with shared state and presence.
Includes conflict resolution and offline support.
"""

import { useEffect, useCallback, useRef } from 'react';
import * as Y from 'yjs';
import { WebrtcProvider } from 'y-webrtc';
import { IndexeddbPersistence } from 'y-indexeddb';
import { usePresence } from '@y-presence/react';
import { Awareness } from 'y-protocols/awareness';
import { nanoid } from 'nanoid';

// Types
export interface CollaborationConfig {
    room: string;
    user: {
        id: string;
        name: string;
        avatar?: string;
    };
    persistence?: boolean;
    offline?: boolean;
    conflict?: 'last-write' | 'merge';
}

export interface PresenceData {
    user: {
        id: string;
        name: string;
        avatar?: string;
    };
    cursor?: {
        x: number;
        y: number;
    };
    selection?: {
        start: number;
        end: number;
    };
    status: 'active' | 'idle' | 'offline';
}

// Collaboration Provider
export function useCollaboration(config: CollaborationConfig) {
    const doc = useRef<Y.Doc>(new Y.Doc());
    const provider = useRef<WebrtcProvider | null>(null);
    const persistence = useRef<IndexeddbPersistence | null>(null);

    // Initialize collaboration
    useEffect(() => {
        // WebRTC provider
        provider.current = new WebrtcProvider(config.room, doc.current);

        // Persistence
        if (config.persistence) {
            persistence.current = new IndexeddbPersistence(
                config.room,
                doc.current
            );
        }

        return () => {
            provider.current?.destroy();
            persistence.current?.destroy();
        };
    }, [config.room]);

    // Shared state
    const sharedState = useCallback((key: string) => {
        return doc.current.getMap(key);
    }, []);

    // Presence
    const { awareness } = provider.current || {};
    const presence = usePresence(awareness as Awareness);

    const updatePresence = useCallback((data: Partial<PresenceData>) => {
        if (awareness) {
            awareness.setLocalState({
                ...awareness.getLocalState(),
                ...data
            });
        }
    }, [awareness]);

    // Conflict resolution
    const resolveConflict = useCallback((
        local: any,
        remote: any
    ) => {
        if (config.conflict === 'last-write') {
            return remote;
        }
        return mergeChanges(local, remote);
    }, [config.conflict]);

    return {
        doc: doc.current,
        sharedState,
        presence,
        updatePresence,
        resolveConflict
    };
}

// Shared Text Editor
export function useSharedText(
    config: CollaborationConfig & {
        initialText?: string;
    }
) {
    const { doc, sharedState } = useCollaboration(config);
    const text = useRef<Y.Text>(doc.getText('shared-text'));

    // Initialize text
    useEffect(() => {
        if (config.initialText && text.current.length === 0) {
            text.current.insert(0, config.initialText);
        }
    }, [config.initialText]);

    // Text operations
    const insert = useCallback((index: number, content: string) => {
        text.current.insert(index, content);
    }, []);

    const delete_ = useCallback((index: number, length: number) => {
        text.current.delete(index, length);
    }, []);

    const format = useCallback((
        index: number,
        length: number,
        format: object
    ) => {
        text.current.format(index, length, format);
    }, []);

    return {
        text: text.current,
        insert,
        delete: delete_,
        format
    };
}

// Shared Drawing Canvas
export function useSharedCanvas(
    config: CollaborationConfig & {
        width: number;
        height: number;
    }
) {
    const { doc, sharedState } = useCollaboration(config);
    const strokes = useRef<Y.Array<any>>(doc.getArray('canvas-strokes'));

    // Stroke operations
    const addStroke = useCallback((stroke: any) => {
        strokes.current.push([stroke]);
    }, []);

    const undoStroke = useCallback(() => {
        strokes.current.delete(strokes.current.length - 1, 1);
    }, []);

    const clearCanvas = useCallback(() => {
        strokes.current.delete(0, strokes.current.length);
    }, []);

    return {
        strokes: strokes.current,
        addStroke,
        undoStroke,
        clearCanvas
    };
}

// Shared Cursors
export function useSharedCursors(config: CollaborationConfig) {
    const { presence, updatePresence } = useCollaboration(config);

    // Update cursor position
    const updateCursor = useCallback((x: number, y: number) => {
        updatePresence({
            cursor: { x, y }
        });
    }, [updatePresence]);

    // Get other users' cursors
    const otherCursors = Object.entries(presence)
        .filter(([id]) => id !== config.user.id)
        .map(([id, data]) => ({
            id,
            ...data.cursor,
            user: data.user
        }));

    return {
        updateCursor,
        otherCursors
    };
}

// Shared Selection
export function useSharedSelection(config: CollaborationConfig) {
    const { presence, updatePresence } = useCollaboration(config);

    // Update selection
    const updateSelection = useCallback((
        start: number,
        end: number
    ) => {
        updatePresence({
            selection: { start, end }
        });
    }, [updatePresence]);

    // Get other users' selections
    const otherSelections = Object.entries(presence)
        .filter(([id]) => id !== config.user.id)
        .map(([id, data]) => ({
            id,
            ...data.selection,
            user: data.user
        }));

    return {
        updateSelection,
        otherSelections
    };
}

// Offline Support
export function useOfflineSync(config: CollaborationConfig) {
    const { doc, sharedState } = useCollaboration(config);

    // Track connection status
    const [isOnline, setIsOnline] = useState(true);

    useEffect(() => {
        const handleOnline = () => setIsOnline(true);
        const handleOffline = () => setIsOnline(false);

        window.addEventListener('online', handleOnline);
        window.addEventListener('offline', handleOffline);

        return () => {
            window.removeEventListener('online', handleOnline);
            window.removeEventListener('offline', handleOffline);
        };
    }, []);

    // Queue offline changes
    const offlineQueue = useRef<any[]>([]);

    const queueChange = useCallback((change: any) => {
        if (!isOnline) {
            offlineQueue.current.push(change);
        }
    }, [isOnline]);

    // Sync when back online
    useEffect(() => {
        if (isOnline && offlineQueue.current.length > 0) {
            const changes = offlineQueue.current;
            offlineQueue.current = [];

            changes.forEach(change => {
                applyChange(doc, change);
            });
        }
    }, [isOnline, doc]);

    return {
        isOnline,
        queueChange
    };
}

// Utilities
function mergeChanges(local: any, remote: any): any {
    // Implement three-way merge
    return merged;
}

function applyChange(doc: Y.Doc, change: any): void {
    // Apply change to doc
}

// Example Usage:
/*
function CollaborativeEditor() {
  const config = {
    room: 'my-doc',
    user: {
      id: nanoid(),
      name: 'User',
      avatar: 'avatar.png'
    },
    persistence: true,
    offline: true,
    conflict: 'merge'
  };
  
  const { text, insert, delete: del } = useSharedText(config);
  const { updateCursor, otherCursors } = useSharedCursors(config);
  const { updateSelection, otherSelections } = useSharedSelection(config);
  const { isOnline, queueChange } = useOfflineSync(config);
  
  return (
    <div>
      <Editor
        text={text}
        onInsert={insert}
        onDelete={del}
        onCursorMove={updateCursor}
        onSelect={updateSelection}
        otherCursors={otherCursors}
        otherSelections={otherSelections}
        isOnline={isOnline}
      />
    </div>
  );
}

function CollaborativeCanvas() {
  const config = {
    room: 'my-canvas',
    user: {
      id: nanoid(),
      name: 'User',
      avatar: 'avatar.png'
    },
    width: 800,
    height: 600
  };
  
  const { strokes, addStroke, undoStroke, clearCanvas } = useSharedCanvas(config);
  const { updateCursor, otherCursors } = useSharedCursors(config);
  
  return (
    <Canvas
      strokes={strokes}
      onStroke={addStroke}
      onUndo={undoStroke}
      onClear={clearCanvas}
      onCursorMove={updateCursor}
      otherCursors={otherCursors}
    />
  );
}
*/ 