"""
Accessibility system with ARIA support and keyboard navigation.
Includes focus management and screen reader optimization.
"""

import { useRef, useEffect, useCallback, createContext, useContext } from 'react';
import { useId } from '@reach/auto-id';
import { FocusScope, useFocusManager } from '@react-aria/focus';
import { useKeyboard } from '@react-aria/interactions';

// Types
export interface A11yConfig {
    role?: string;
    label?: string;
    description?: string;
    keyboardShortcuts?: string[];
    focusable?: boolean;
    autoFocus?: boolean;
    tabIndex?: number;
    live?: 'off' | 'polite' | 'assertive';
}

export interface A11yState {
    focused: boolean;
    hovered: boolean;
    pressed: boolean;
    selected: boolean;
    expanded: boolean;
    disabled: boolean;
}

// Context
const A11yContext = createContext<{
    registerComponent: (id: string, config: A11yConfig) => void;
    unregisterComponent: (id: string) => void;
    getState: (id: string) => A11yState;
    setState: (id: string, state: Partial<A11yState>) => void;
} | null>(null);

// Provider
export function A11yProvider({ children }: { children: React.ReactNode }) {
    const components = useRef<Map<string, A11yConfig>>(new Map());
    const states = useRef<Map<string, A11yState>>(new Map());

    const registerComponent = useCallback((id: string, config: A11yConfig) => {
        components.current.set(id, config);
        states.current.set(id, {
            focused: false,
            hovered: false,
            pressed: false,
            selected: false,
            expanded: false,
            disabled: false
        });
    }, []);

    const unregisterComponent = useCallback((id: string) => {
        components.current.delete(id);
        states.current.delete(id);
    }, []);

    const getState = useCallback((id: string) => {
        return states.current.get(id) || {
            focused: false,
            hovered: false,
            pressed: false,
            selected: false,
            expanded: false,
            disabled: false
        };
    }, []);

    const setState = useCallback((id: string, state: Partial<A11yState>) => {
        const currentState = states.current.get(id);
        if (currentState) {
            states.current.set(id, { ...currentState, ...state });
        }
    }, []);

    return (
        <A11yContext.Provider
      value= {{ registerComponent, unregisterComponent, getState, setState }
}
    >
    { children }
    </A11yContext.Provider>
  );
}

// Hooks
export function useA11y(config: A11yConfig = {}) {
    const context = useContext(A11yContext);
    const id = useId();
    const ref = useRef<HTMLElement>(null);
    const focusManager = useFocusManager();

    useEffect(() => {
        if (id && context) {
            context.registerComponent(id, config);
            return () => context.unregisterComponent(id);
        }
    }, [id, context, config]);

    const { keyboardProps } = useKeyboard({
        onKeyDown: (e) => {
            if (e.key === 'Enter' || e.key === ' ') {
                e.preventDefault();
                ref.current?.click();
            }
        }
    });

    const getA11yProps = () => ({
        ref,
        id,
        role: config.role,
        'aria-label': config.label,
        'aria-description': config.description,
        'aria-keyshortcuts': config.keyboardShortcuts?.join(' '),
        tabIndex: config.focusable ? config.tabIndex || 0 : -1,
        'aria-live': config.live,
        ...keyboardProps,
        onFocus: () => context?.setState(id, { focused: true }),
        onBlur: () => context?.setState(id, { focused: false }),
        onMouseEnter: () => context?.setState(id, { hovered: true }),
        onMouseLeave: () => context?.setState(id, { hovered: false }),
        onMouseDown: () => context?.setState(id, { pressed: true }),
        onMouseUp: () => context?.setState(id, { pressed: false })
    });

    return {
        ref,
        id,
        state: context?.getState(id),
        getA11yProps,
        focusManager
    };
}

// Focus Management
export function FocusContainer({ children }: { children: React.ReactNode }) {
    return (
        <FocusScope>
        { children }
        </FocusScope>
    );
}

// Screen Reader Announcements
export function useAnnounce() {
    const announcePolite = useCallback((message: string) => {
        const element = document.createElement('div');
        element.setAttribute('role', 'status');
        element.setAttribute('aria-live', 'polite');
        element.textContent = message;
        document.body.appendChild(element);
        setTimeout(() => document.body.removeChild(element), 1000);
    }, []);

    const announceAssertive = useCallback((message: string) => {
        const element = document.createElement('div');
        element.setAttribute('role', 'alert');
        element.setAttribute('aria-live', 'assertive');
        element.textContent = message;
        document.body.appendChild(element);
        setTimeout(() => document.body.removeChild(element), 1000);
    }, []);

    return { announcePolite, announceAssertive };
}

// Keyboard Navigation
export function useKeyboardNavigation(
    containerRef: React.RefObject<HTMLElement>,
    itemSelector: string
) {
    const focusManager = useFocusManager();

    const handleKeyDown = useCallback((e: KeyboardEvent) => {
        const container = containerRef.current;
        if (!container) return;

        const items = Array.from(container.querySelectorAll(itemSelector));
        const currentIndex = items.findIndex((item) => item === document.activeElement);

        switch (e.key) {
            case 'ArrowDown':
            case 'ArrowRight':
                e.preventDefault();
                if (currentIndex < items.length - 1) {
                    (items[currentIndex + 1] as HTMLElement).focus();
                }
                break;
            case 'ArrowUp':
            case 'ArrowLeft':
                e.preventDefault();
                if (currentIndex > 0) {
                    (items[currentIndex - 1] as HTMLElement).focus();
                }
                break;
            case 'Home':
                e.preventDefault();
                (items[0] as HTMLElement).focus();
                break;
            case 'End':
                e.preventDefault();
                (items[items.length - 1] as HTMLElement).focus();
                break;
        }
    }, [containerRef, itemSelector]);

    useEffect(() => {
        const container = containerRef.current;
        if (container) {
            container.addEventListener('keydown', handleKeyDown);
            return () => container.removeEventListener('keydown', handleKeyDown);
        }
    }, [containerRef, handleKeyDown]);

    return { focusManager };
}

// Example Usage:
/*
function AccessibleButton({ children, onClick }: ButtonProps) {
  const { getA11yProps, state } = useA11y({
    role: 'button',
    label: 'Accessible Button',
    focusable: true,
    keyboardShortcuts: ['Enter', 'Space']
  });

  return (
    <button
      {...getA11yProps()}
      onClick={onClick}
      className={`button ${state?.focused ? 'focused' : ''}`}
    >
      {children}
    </button>
  );
}

function AccessibleMenu() {
  const containerRef = useRef<HTMLUListElement>(null);
  useKeyboardNavigation(containerRef, '[role="menuitem"]');

  return (
    <FocusContainer>
      <ul ref={containerRef} role="menu">
        <li role="menuitem" tabIndex={0}>Item 1</li>
        <li role="menuitem" tabIndex={0}>Item 2</li>
        <li role="menuitem" tabIndex={0}>Item 3</li>
      </ul>
    </FocusContainer>
  );
}
*/ 