"""
Advanced theming system with dynamic themes and CSS -in -JS.
Includes theme inheritance, variants, and runtime updates.
"""

import { createContext, useContext, useEffect, useMemo } from 'react';
import { css } from '@emotion/react';
import Color from 'color';

// Types
export interface ThemeToken {
    value: string | number;
    type: 'color' | 'spacing' | 'typography' | 'shadow' | 'animation';
    variants?: Record<string, string | number>;
    scale?: Record<string, string | number>;
}

export interface ThemeConfig {
    name: string;
    extends?: string;
    tokens: Record<string, ThemeToken>;
    variants?: Record<string, Record<string, any>>;
    breakpoints?: Record<string, number>;
    colorScheme?: 'light' | 'dark' | 'system';
}

// Theme Context
const ThemeContext = createContext<{
    theme: ThemeConfig;
    updateTheme: (updates: Partial<ThemeConfig>) => void;
    setColorScheme: (scheme: 'light' | 'dark' | 'system') => void;
} | null>(null);

// Theme Provider
export function ThemeProvider({
    children,
    initial
}: {
    children: React.ReactNode;
    initial: ThemeConfig;
}) {
    const [theme, setTheme] = useState(initial);

    // Update theme
    const updateTheme = useCallback((updates: Partial<ThemeConfig>) => {
        setTheme(current => ({
            ...current,
            ...updates,
            tokens: {
                ...current.tokens,
                ...updates.tokens
            }
        }));
    }, []);

    // Color scheme
    const setColorScheme = useCallback((
        scheme: 'light' | 'dark' | 'system'
    ) => {
        updateTheme({ colorScheme: scheme });
    }, [updateTheme]);

    // System color scheme
    useEffect(() => {
        if (theme.colorScheme === 'system') {
            const media = window.matchMedia('(prefers-color-scheme: dark)');
            const handler = () => {
                updateTheme({
                    tokens: generateSystemTokens(theme.tokens, media.matches)
                });
            };

            media.addEventListener('change', handler);
            handler();

            return () => media.removeEventListener('change', handler);
        }
    }, [theme.colorScheme, updateTheme]);

    return (
        <ThemeContext.Provider
      value= {{ theme, updateTheme, setColorScheme }
}
    >
    { children }
    </ThemeContext.Provider>
  );
}

// Theme Hook
export function useTheme() {
    const context = useContext(ThemeContext);
    if (!context) {
        throw new Error('useTheme must be used within ThemeProvider');
    }
    return context;
}

// Token System
export function useToken(
    tokenName: string,
    variant?: string,
    scale?: string
) {
    const { theme } = useTheme();

    return useMemo(() => {
        const token = theme.tokens[tokenName];
        if (!token) return null;

        if (variant && token.variants?.[variant]) {
            return token.variants[variant];
        }

        if (scale && token.scale?.[scale]) {
            return token.scale[scale];
        }

        return token.value;
    }, [theme, tokenName, variant, scale]);
}

// CSS-in-JS
export function useStyles(styles: Record<string, any>) {
    const { theme } = useTheme();

    return useMemo(() => {
        const processedStyles = Object.entries(styles).reduce(
            (acc, [key, value]) => ({
                ...acc,
                [key]: processStyle(value, theme)
            }),
            {}
        );

        return css(processedStyles);
    }, [theme, styles]);
}

// Variant System
export function useVariant(
    component: string,
    variant: string
) {
    const { theme } = useTheme();

    return useMemo(() => {
        const variants = theme.variants?.[component];
        if (!variants) return {};

        return variants[variant] || {};
    }, [theme, component, variant]);
}

// Color Manipulation
export function useColor(color: string) {
    const processedColor = useMemo(() => {
        const c = Color(color);

        return {
            lighten: (amount: number) => c.lighten(amount).toString(),
            darken: (amount: number) => c.darken(amount).toString(),
            alpha: (amount: number) => c.alpha(amount).toString(),
            mix: (other: string, amount: number) => (
                c.mix(Color(other), amount).toString()
            )
        };
    }, [color]);

    return processedColor;
}

// Responsive System
export function useBreakpoint(breakpoint: string) {
    const { theme } = useTheme();
    const [matches, setMatches] = useState(false);

    useEffect(() => {
        const width = theme.breakpoints?.[breakpoint];
        if (!width) return;

        const media = window.matchMedia(`(min-width: ${width}px)`);
        const handler = () => setMatches(media.matches);

        media.addEventListener('change', handler);
        handler();

        return () => media.removeEventListener('change', handler);
    }, [theme, breakpoint]);

    return matches;
}

// Theme Generation
export function generateTheme(config: Partial<ThemeConfig>): ThemeConfig {
    const base = defaultTheme;

    if (config.extends) {
        const parent = themes[config.extends];
        if (parent) {
            return mergeThemes(parent, config);
        }
    }

    return mergeThemes(base, config);
}

// Utilities
function processStyle(
    style: any,
    theme: ThemeConfig
): any {
    if (typeof style === 'string' && style.startsWith('$')) {
        const token = style.slice(1);
        return theme.tokens[token]?.value;
    }

    if (typeof style === 'object') {
        return Object.entries(style).reduce(
            (acc, [key, value]) => ({
                ...acc,
                [key]: processStyle(value, theme)
            }),
            {}
        );
    }

    return style;
}

function mergeThemes(
    base: ThemeConfig,
    override: Partial<ThemeConfig>
): ThemeConfig {
    return {
        ...base,
        ...override,
        tokens: {
            ...base.tokens,
            ...override.tokens
        },
        variants: {
            ...base.variants,
            ...override.variants
        },
        breakpoints: {
            ...base.breakpoints,
            ...override.breakpoints
        }
    };
}

function generateSystemTokens(
    tokens: Record<string, ThemeToken>,
    isDark: boolean
): Record<string, ThemeToken> {
    return Object.entries(tokens).reduce(
        (acc, [key, token]) => {
            if (token.type === 'color') {
                const color = Color(token.value.toString());
                acc[key] = {
                    ...token,
                    value: isDark ? color.darken(0.2).toString() : token.value
                };
            } else {
                acc[key] = token;
            }
            return acc;
        },
        {} as Record<string, ThemeToken>
    );
}

// Default Theme
const defaultTheme: ThemeConfig = {
    name: 'default',
    colorScheme: 'system',
    tokens: {
        // Colors
        primary: {
            value: '#0066FF',
            type: 'color',
            variants: {
                light: '#3385FF',
                dark: '#0052CC'
            },
            scale: {
                100: '#E6F0FF',
                200: '#CCE0FF',
                300: '#99C2FF',
                400: '#66A3FF',
                500: '#3385FF',
                600: '#0066FF',
                700: '#0052CC',
                800: '#003D99',
                900: '#002966'
            }
        },

        // Typography
        fontFamily: {
            value: 'Inter, system-ui, sans-serif',
            type: 'typography'
        },
        fontSize: {
            value: '16px',
            type: 'typography',
            scale: {
                xs: '12px',
                sm: '14px',
                md: '16px',
                lg: '18px',
                xl: '20px',
                '2xl': '24px',
                '3xl': '30px',
                '4xl': '36px'
            }
        },

        // Spacing
        spacing: {
            value: '4px',
            type: 'spacing',
            scale: {
                xs: '4px',
                sm: '8px',
                md: '16px',
                lg: '24px',
                xl: '32px',
                '2xl': '48px',
                '3xl': '64px',
                '4xl': '96px'
            }
        },

        // Shadows
        shadow: {
            value: '0 2px 4px rgba(0,0,0,0.1)',
            type: 'shadow',
            variants: {
                sm: '0 1px 2px rgba(0,0,0,0.05)',
                md: '0 4px 6px rgba(0,0,0,0.1)',
                lg: '0 10px 15px rgba(0,0,0,0.1)',
                xl: '0 20px 25px rgba(0,0,0,0.1)'
            }
        },

        // Animations
        transition: {
            value: '200ms ease-in-out',
            type: 'animation',
            variants: {
                fast: '100ms ease-in-out',
                slow: '300ms ease-in-out'
            }
        }
    },

    // Component Variants
    variants: {
        button: {
            primary: {
                backgroundColor: '$primary',
                color: 'white',
                padding: '$spacing.md',
                borderRadius: '$spacing.xs',
                transition: '$transition'
            },
            secondary: {
                backgroundColor: 'transparent',
                color: '$primary',
                border: '1px solid $primary',
                padding: '$spacing.md',
                borderRadius: '$spacing.xs',
                transition: '$transition'
            }
        }
    },

    // Breakpoints
    breakpoints: {
        sm: 640,
        md: 768,
        lg: 1024,
        xl: 1280,
        '2xl': 1536
    }
};

// Theme Registry
const themes: Record<string, ThemeConfig> = {
    default: defaultTheme
};

// Example Usage:
/*
function App() {
  const theme = generateTheme({
    name: 'custom',
    extends: 'default',
    colorScheme: 'system',
    tokens: {
      primary: {
        value: '#FF0066',
        type: 'color'
      }
    }
  });
  
  return (
    <ThemeProvider initial={theme}>
      <ThemedComponent />
    </ThemeProvider>
  );
}

function ThemedComponent() {
  const primary = useToken('primary');
  const buttonVariant = useVariant('button', 'primary');
  const color = useColor(primary);
  const isDesktop = useBreakpoint('lg');
  
  const styles = useStyles({
    container: {
      backgroundColor: color.lighten(0.2),
      padding: '$spacing.lg',
      ...buttonVariant
    },
    text: {
      fontSize: isDesktop ? '$fontSize.xl' : '$fontSize.md'
    }
  });
  
  return (
    <div css={styles.container}>
      <p css={styles.text}>Themed Component</p>
    </div>
  );
}
*/ 