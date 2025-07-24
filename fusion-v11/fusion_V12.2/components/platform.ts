"""
Cross - platform adaptation system for components.
Includes platform detection, feature detection, and adaptive rendering.
"""

import { useEffect, useMemo, useCallback } from 'react';
import UAParser from 'ua-parser-js';

// Types
export interface PlatformInfo {
    os: {
        name: string;
        version: string;
    };
    browser: {
        name: string;
        version: string;
    };
    device: {
        type: 'mobile' | 'tablet' | 'desktop';
        vendor?: string;
        model?: string;
    };
    engine: {
        name: string;
        version: string;
    };
}

export interface PlatformCapabilities {
    touch: boolean;
    hover: boolean;
    pointer: boolean;
    keyboard: boolean;
    webgl: boolean;
    webgl2: boolean;
    webp: boolean;
    webm: boolean;
    hevc: boolean;
    vp9: boolean;
}

export interface PlatformConstraints {
    minWidth?: number;
    maxWidth?: number;
    minHeight?: number;
    maxHeight?: number;
    orientation?: 'portrait' | 'landscape';
    aspectRatio?: number;
    pixelRatio?: number;
}

// Platform Detection
export function usePlatform(): PlatformInfo {
    return useMemo(() => {
        const parser = new UAParser();
        const result = parser.getResult();

        return {
            os: {
                name: result.os.name || 'unknown',
                version: result.os.version || 'unknown'
            },
            browser: {
                name: result.browser.name || 'unknown',
                version: result.browser.version || 'unknown'
            },
            device: {
                type: getDeviceType(result),
                vendor: result.device.vendor,
                model: result.device.model
            },
            engine: {
                name: result.engine.name || 'unknown',
                version: result.engine.version || 'unknown'
            }
        };
    }, []);
}

// Feature Detection
export function useCapabilities(): PlatformCapabilities {
    return useMemo(() => ({
        touch: 'ontouchstart' in window,
        hover: matchMedia('(hover: hover)').matches,
        pointer: matchMedia('(pointer: fine)').matches,
        keyboard: 'onkeydown' in window,
        webgl: hasWebGL(),
        webgl2: hasWebGL2(),
        webp: hasWebP(),
        webm: hasWebM(),
        hevc: hasHEVC(),
        vp9: hasVP9()
    }), []);
}

// Adaptive Rendering
export function useAdaptiveRender(
    constraints: PlatformConstraints
): boolean {
    const [matches, setMatches] = useState(true);

    useEffect(() => {
        const queries: string[] = [];

        if (constraints.minWidth) {
            queries.push(`(min-width: ${constraints.minWidth}px)`);
        }
        if (constraints.maxWidth) {
            queries.push(`(max-width: ${constraints.maxWidth}px)`);
        }
        if (constraints.minHeight) {
            queries.push(`(min-height: ${constraints.minHeight}px)`);
        }
        if (constraints.maxHeight) {
            queries.push(`(max-height: ${constraints.maxHeight}px)`);
        }
        if (constraints.orientation) {
            queries.push(`(orientation: ${constraints.orientation})`);
        }
        if (constraints.aspectRatio) {
            queries.push(`(aspect-ratio: ${constraints.aspectRatio})`);
        }
        if (constraints.pixelRatio) {
            queries.push(`(device-pixel-ratio: ${constraints.pixelRatio})`);
        }

        const query = queries.join(' and ');
        const media = window.matchMedia(query);

        const handler = () => setMatches(media.matches);
        media.addEventListener('change', handler);
        handler();

        return () => media.removeEventListener('change', handler);
    }, [constraints]);

    return matches;
}

// Platform-Specific Components
export function PlatformComponent<T>({
    mobile,
    tablet,
    desktop,
    fallback
}: {
    mobile?: React.ComponentType<T>;
    tablet?: React.ComponentType<T>;
    desktop?: React.ComponentType<T>;
    fallback?: React.ComponentType<T>;
}) {
    const { device } = usePlatform();

    const Component = useMemo(() => {
        switch (device.type) {
            case 'mobile':
                return mobile || fallback;
            case 'tablet':
                return tablet || fallback;
            case 'desktop':
                return desktop || fallback;
            default:
                return fallback;
        }
    }, [device.type, mobile, tablet, desktop, fallback]);

    return Component ? <Component /> : null;
}

// Platform-Specific Styles
export function usePlatformStyles<T extends object>(
    styles: Record<'mobile' | 'tablet' | 'desktop', T>
): T {
    const { device } = usePlatform();

    return useMemo(() => {
        switch (device.type) {
            case 'mobile':
                return styles.mobile;
            case 'tablet':
                return styles.tablet;
            case 'desktop':
                return styles.desktop;
            default:
                return styles.desktop;
        }
    }, [device.type, styles]);
}

// Platform-Specific Behavior
export function usePlatformBehavior<T>(
    behaviors: Record<'mobile' | 'tablet' | 'desktop', T>
): T {
    const { device } = usePlatform();

    return useMemo(() => {
        switch (device.type) {
            case 'mobile':
                return behaviors.mobile;
            case 'tablet':
                return behaviors.tablet;
            case 'desktop':
                return behaviors.desktop;
            default:
                return behaviors.desktop;
        }
    }, [device.type, behaviors]);
}

// Utilities
function getDeviceType(result: UAParser.IResult): 'mobile' | 'tablet' | 'desktop' {
    if (result.device.type === 'mobile') return 'mobile';
    if (result.device.type === 'tablet') return 'tablet';
    return 'desktop';
}

function hasWebGL(): boolean {
    try {
        const canvas = document.createElement('canvas');
        return !!(
            window.WebGLRenderingContext &&
            (canvas.getContext('webgl') ||
                canvas.getContext('experimental-webgl'))
        );
    } catch (e) {
        return false;
    }
}

function hasWebGL2(): boolean {
    try {
        const canvas = document.createElement('canvas');
        return !!(window.WebGL2RenderingContext && canvas.getContext('webgl2'));
    } catch (e) {
        return false;
    }
}

async function hasWebP(): Promise<boolean> {
    const webP = new Image();
    webP.src = 'data:image/webp;base64,UklGRjoAAABXRUJQVlA4IC4AAACyAgCdASoCAAIALmk0mk0iIiIiIgBoSygABc6WWgAA/veff/0PP8bA//LwYAAA';
    return new Promise(resolve => {
        webP.onload = webP.onerror = () => {
            resolve(webP.height === 2);
        };
    });
}

function hasWebM(): boolean {
    const video = document.createElement('video');
    return video.canPlayType('video/webm; codecs="vp8, vorbis"') !== '';
}

function hasHEVC(): boolean {
    const video = document.createElement('video');
    return video.canPlayType('video/mp4; codecs="hevc,mp4a.40.2"') !== '';
}

function hasVP9(): boolean {
    const video = document.createElement('video');
    return video.canPlayType('video/webm; codecs="vp9"') !== '';
}

// Example Usage:
/*
function AdaptiveComponent() {
  const platform = usePlatform();
  const capabilities = useCapabilities();
  const matches = useAdaptiveRender({
    minWidth: 768,
    orientation: 'landscape'
  });
  
  const styles = usePlatformStyles({
    mobile: {
      fontSize: '14px',
      padding: '8px'
    },
    tablet: {
      fontSize: '16px',
      padding: '16px'
    },
    desktop: {
      fontSize: '18px',
      padding: '24px'
    }
  });
  
  const behavior = usePlatformBehavior({
    mobile: {
      onClick: () => console.log('Mobile click'),
      onTouch: () => console.log('Mobile touch')
    },
    tablet: {
      onClick: () => console.log('Tablet click'),
      onTouch: () => console.log('Tablet touch')
    },
    desktop: {
      onClick: () => console.log('Desktop click'),
      onHover: () => console.log('Desktop hover')
    }
  });
  
  return (
    <div style={styles} {...behavior}>
      <PlatformComponent
        mobile={MobileView}
        tablet={TabletView}
        desktop={DesktopView}
        fallback={FallbackView}
      />
    </div>
  );
}
*/ 