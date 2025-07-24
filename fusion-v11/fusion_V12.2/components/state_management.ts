"""
Advanced state management system for React components.
Includes hooks, context, and state machines.
"""

import { createContext, useContext, useReducer, useCallback, useRef, useEffect } from 'react';
import { createMachine, interpret } from '@xstate/fsm';
import { atom, useAtom } from 'jotai';
import { atomWithStorage } from 'jotai/utils';

// Types
export interface ComponentState {
    value: any;
    variant: string;
    disabled: boolean;
    loading: boolean;
    error?: string;
    metadata: Record<string, any>;
}

export interface StateAction {
    type: string;
    payload?: any;
}

export interface StateConfig {
    initialState: ComponentState;
    persistKey?: string;
    stateMachine?: boolean;
    atomicState?: boolean;
}

// Context
const StateContext = createContext<{
    state: ComponentState;
    dispatch: (action: StateAction) => void;
} | null>(null);

// Reducer
function stateReducer(state: ComponentState, action: StateAction): ComponentState {
    switch (action.type) {
        case 'SET_VALUE':
            return { ...state, value: action.payload };
        case 'SET_VARIANT':
            return { ...state, variant: action.payload };
        case 'SET_DISABLED':
            return { ...state, disabled: action.payload };
        case 'SET_LOADING':
            return { ...state, loading: action.payload };
        case 'SET_ERROR':
            return { ...state, error: action.payload };
        case 'SET_METADATA':
            return {
                ...state,
                metadata: { ...state.metadata, ...action.payload }
            };
        case 'RESET':
            return action.payload;
        default:
            return state;
    }
}

// State Machine
const createComponentMachine = (config: StateConfig) => createMachine({
    id: 'component',
    initial: 'idle',
    states: {
        idle: {
            on: {
                HOVER: 'hovered',
                DISABLE: 'disabled',
                LOAD: 'loading'
            }
        },
        hovered: {
            on: {
                UNHOVER: 'idle',
                DISABLE: 'disabled',
                LOAD: 'loading'
            }
        },
        disabled: {
            on: {
                ENABLE: 'idle'
            }
        },
        loading: {
            on: {
                LOADED: 'idle',
                ERROR: 'error'
            }
        },
        error: {
            on: {
                RETRY: 'loading',
                RESET: 'idle'
            }
        }
    }
});

// Atomic State
const createComponentAtom = (config: StateConfig) => {
    const baseAtom = config.persistKey
        ? atomWithStorage(config.persistKey, config.initialState)
        : atom(config.initialState);

    return {
        baseAtom,
        valueAtom: atom(
            (get) => get(baseAtom).value,
            (get, set, value: any) => set(baseAtom, {
                ...get(baseAtom),
                value
            })
        ),
        variantAtom: atom(
            (get) => get(baseAtom).variant,
            (get, set, variant: string) => set(baseAtom, {
                ...get(baseAtom),
                variant
            })
        )
    };
};

// Provider
export function StateProvider({
    children,
    config
}: {
    children: React.ReactNode;
    config: StateConfig;
}) {
    const [state, dispatch] = useReducer(stateReducer, config.initialState);

    return (
        <StateContext.Provider value= {{ state, dispatch }
}>
    { children }
    </StateContext.Provider>
  );
}

// Hooks
export function useComponentState(config: StateConfig) {
    const context = useContext(StateContext);
    const machineRef = useRef(interpret(createComponentMachine(config)));
    const [atomState, setAtomState] = useAtom(createComponentAtom(config).baseAtom);

    useEffect(() => {
        if (config.stateMachine) {
            machineRef.current.start();
            return () => machineRef.current.stop();
        }
    }, [config.stateMachine]);

    const setState = useCallback((value: any) => {
        if (config.atomicState) {
            setAtomState((prev) => ({ ...prev, value }));
        } else {
            context?.dispatch({ type: 'SET_VALUE', payload: value });
        }
    }, [config.atomicState, context, setAtomState]);

    const setVariant = useCallback((variant: string) => {
        if (config.atomicState) {
            setAtomState((prev) => ({ ...prev, variant }));
        } else {
            context?.dispatch({ type: 'SET_VARIANT', payload: variant });
        }
    }, [config.atomicState, context, setAtomState]);

    const setDisabled = useCallback((disabled: boolean) => {
        if (config.stateMachine) {
            machineRef.current.send(disabled ? 'DISABLE' : 'ENABLE');
        } else if (config.atomicState) {
            setAtomState((prev) => ({ ...prev, disabled }));
        } else {
            context?.dispatch({ type: 'SET_DISABLED', payload: disabled });
        }
    }, [config.stateMachine, config.atomicState, context, setAtomState]);

    const setLoading = useCallback((loading: boolean) => {
        if (config.stateMachine) {
            machineRef.current.send(loading ? 'LOAD' : 'LOADED');
        } else if (config.atomicState) {
            setAtomState((prev) => ({ ...prev, loading }));
        } else {
            context?.dispatch({ type: 'SET_LOADING', payload: loading });
        }
    }, [config.stateMachine, config.atomicState, context, setAtomState]);

    const setError = useCallback((error: string | undefined) => {
        if (config.stateMachine) {
            machineRef.current.send(error ? 'ERROR' : 'RESET');
        } else if (config.atomicState) {
            setAtomState((prev) => ({ ...prev, error }));
        } else {
            context?.dispatch({ type: 'SET_ERROR', payload: error });
        }
    }, [config.stateMachine, config.atomicState, context, setAtomState]);

    const reset = useCallback(() => {
        if (config.stateMachine) {
            machineRef.current.send('RESET');
        } else if (config.atomicState) {
            setAtomState(config.initialState);
        } else {
            context?.dispatch({ type: 'RESET', payload: config.initialState });
        }
    }, [config.stateMachine, config.atomicState, config.initialState, context, setAtomState]);

    return {
        state: config.atomicState ? atomState : context?.state,
        setState,
        setVariant,
        setDisabled,
        setLoading,
        setError,
        reset,
        machine: config.stateMachine ? machineRef.current : undefined
    };
}

// Example Usage:
/*
function MyComponent() {
  const { state, setState, setVariant, setDisabled } = useComponentState({
    initialState: {
      value: '',
      variant: 'default',
      disabled: false,
      loading: false,
      metadata: {}
    },
    persistKey: 'myComponent',  // Optional: persist state
    stateMachine: true,        // Optional: use state machine
    atomicState: true         // Optional: use atomic state
  });

  return (
    <div>
      <input
        value={state.value}
        onChange={(e) => setState(e.target.value)}
        disabled={state.disabled}
      />
      <button onClick={() => setVariant('hover')}>
        Hover
      </button>
      <button onClick={() => setDisabled(!state.disabled)}>
        Toggle Disabled
      </button>
    </div>
  );
}
*/ 