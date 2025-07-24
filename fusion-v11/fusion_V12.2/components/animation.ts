"""
Animation system with Framer Motion integration.
Includes preset animations and custom variants.
"""

import { motion, AnimatePresence, useAnimation } from 'framer-motion';
import { useCallback, useEffect, useMemo } from 'react';

// Types
export interface AnimationConfig {
    preset?: string;
    duration?: number;
    ease?: string;
    delay?: number;
    repeat?: number;
    repeatType?: 'loop' | 'reverse' | 'mirror';
    custom?: Record<string, any>;
}

export interface AnimationVariants {
    initial?: Record<string, any>;
    animate?: Record<string, any>;
    exit?: Record<string, any>;
    hover?: Record<string, any>;
    tap?: Record<string, any>;
    drag?: Record<string, any>;
}

// Preset Animations
export const presets = {
    fadeIn: {
        initial: { opacity: 0 },
        animate: { opacity: 1 },
        exit: { opacity: 0 }
    },
    slideIn: {
        initial: { x: -20, opacity: 0 },
        animate: { x: 0, opacity: 1 },
        exit: { x: 20, opacity: 0 }
    },
    scaleIn: {
        initial: { scale: 0.9, opacity: 0 },
        animate: { scale: 1, opacity: 1 },
        exit: { scale: 0.9, opacity: 0 }
    },
    springIn: {
        initial: { y: -20, opacity: 0 },
        animate: { y: 0, opacity: 1 },
        exit: { y: 20, opacity: 0 }
    },
    popIn: {
        initial: { scale: 0, rotate: -180 },
        animate: { scale: 1, rotate: 0 },
        exit: { scale: 0, rotate: 180 }
    }
};

// Easing Functions
export const easings = {
    smooth: [0.4, 0, 0.2, 1],
    spring: [0.43, 0.13, 0.23, 0.96],
    bounce: [0.68, -0.55, 0.265, 1.55],
    gentle: [0.6, 0.01, 0, 0.99],
    snappy: [0.25, 0.46, 0.45, 0.94]
};

// Animation Hook
export function useComponentAnimation(config: AnimationConfig = {}) {
    const controls = useAnimation();

    const variants = useMemo(() => {
        if (config.preset && presets[config.preset]) {
            return presets[config.preset];
        }
        return {};
    }, [config.preset]);

    const transition = useMemo(() => ({
        duration: config.duration || 0.3,
        ease: config.ease ? easings[config.ease] : easings.smooth,
        delay: config.delay || 0,
        repeat: config.repeat || 0,
        repeatType: config.repeatType || 'loop'
    }), [config]);

    const animate = useCallback(async (animation: string | Record<string, any>) => {
        await controls.start(animation);
    }, [controls]);

    const stop = useCallback(() => {
        controls.stop();
    }, [controls]);

    const reset = useCallback(() => {
        controls.set(variants.initial || {});
    }, [controls, variants]);

    return {
        controls,
        variants,
        transition,
        animate,
        stop,
        reset
    };
}

// Presence Hook
export function useAnimatePresence(visible: boolean, config: AnimationConfig = {}) {
    const { variants, transition } = useComponentAnimation(config);

    return {
        initial: variants.initial,
        animate: visible ? variants.animate : variants.exit,
        exit: variants.exit,
        transition
    };
}

// Gesture Animation Hook
export function useGestureAnimation(config: AnimationConfig = {}) {
    const { variants, transition } = useComponentAnimation(config);

    return {
        whileHover: variants.hover,
        whileTap: variants.tap,
        whileDrag: variants.drag,
        transition
    };
}

// Sequence Animation Hook
export function useSequenceAnimation(
    animations: Array<[string, AnimationConfig]>
) {
    const controls = useAnimation();

    const sequence = useCallback(async () => {
        for (const [name, config] of animations) {
            const { variants, transition } = useComponentAnimation(config);
            await controls.start({
                ...variants.animate,
                transition
            });
        }
    }, [controls, animations]);

    return {
        controls,
        sequence
    };
}

// Example Usage:
/*
function AnimatedComponent({ visible }) {
  const { variants, transition } = useComponentAnimation({
    preset: 'fadeIn',
    duration: 0.5,
    ease: 'spring'
  });

  return (
    <AnimatePresence>
      {visible && (
        <motion.div
          initial={variants.initial}
          animate={variants.animate}
          exit={variants.exit}
          transition={transition}
        >
          Content
        </motion.div>
      )}
    </AnimatePresence>
  );
}

function InteractiveComponent() {
  const gestureProps = useGestureAnimation({
    preset: 'scaleIn',
    duration: 0.2
  });

  return (
    <motion.button
      {...gestureProps}
    >
      Interactive Button
    </motion.button>
  );
}

function SequenceComponent() {
  const { controls, sequence } = useSequenceAnimation([
    ['fadeIn', { duration: 0.3 }],
    ['slideIn', { duration: 0.5, ease: 'spring' }],
    ['scaleIn', { duration: 0.2 }]
  ]);

  useEffect(() => {
    sequence();
  }, []);

  return (
    <motion.div animate={controls}>
      Sequenced Animation
    </motion.div>
  );
}
*/ 