# Real-World Migration and Error Handling Examples

This document provides comprehensive examples of real-world scenarios, including migrations, error handling, and multi-chain orchestration.

## 1. Legacy Design System Migration

### Scenario
Migrating a legacy Material-UI based design system to a new Tailwind-based system.

### Implementation

```typescript
// Legacy Component
interface LegacyButtonProps {
  variant: 'contained' | 'outlined';
  color: 'primary' | 'secondary';
  size: 'small' | 'medium' | 'large';
  onClick: () => void;
}

const LegacyButton: React.FC<LegacyButtonProps> = ({
  variant,
  color,
  size,
  onClick,
  children
}) => (
  <Button
    variant={variant}
    color={color}
    size={size}
    onClick={onClick}
  >
    {children}
  </Button>
);

// Migration Chain Execution
const migrationResult = await executeMigrationChain({
  component: LegacyButton,
  analysis: {
    props: ['variant', 'color', 'size', 'onClick'],
    styles: {
      contained: 'elevated button styles',
      outlined: 'bordered button styles'
    },
    events: ['onClick'],
    accessibility: {
      role: 'button',
      ariaPressed: 'mixed'
    }
  }
});

// New Component
interface NewButtonProps {
  variant: 'solid' | 'outline';
  intent: 'primary' | 'secondary';
  scale: 'sm' | 'md' | 'lg';
  onPress: () => void;
}

const NewButton = React.forwardRef<HTMLButtonElement, NewButtonProps>(({
  variant = 'solid',
  intent = 'primary',
  scale = 'md',
  onPress,
  children
}, ref) => (
  <button
    ref={ref}
    onClick={onPress}
    className={cn(
      buttonVariants({ variant, intent, scale })
    )}
    role="button"
    aria-pressed={false}
  >
    {children}
  </button>
));
```

### Error Recovery
```typescript
try {
  await migrationChain.execute(component);
} catch (error) {
  if (error instanceof IncompatiblePropsError) {
    // Automatically generate prop adapters
    const adapter = await generatePropAdapter(
      error.legacyProps,
      error.newProps
    );
    // Retry with adapter
    await migrationChain.execute(component, { adapter });
  } else if (error instanceof StyleMappingError) {
    // Use style mapping recovery
    const styleMap = await generateStyleMap(
      error.legacyStyles,
      error.newStyles
    );
    // Retry with style map
    await migrationChain.execute(component, { styleMap });
  }
}
```

## 2. Multi-Chain Orchestration

### Scenario
Complex component requiring design system, testing, and documentation chains.

### Implementation

```typescript
// Chain Orchestration
const orchestrationConfig = {
  chains: [
    {
      type: 'design_system',
      dependencies: [],
      output: 'component_spec'
    },
    {
      type: 'testing',
      dependencies: ['design_system'],
      output: 'test_suite'
    },
    {
      type: 'documentation',
      dependencies: ['design_system', 'testing'],
      output: 'docs'
    }
  ],
  errorHandling: {
    retryStrategy: {
      maxAttempts: 3,
      backoff: 'exponential'
    },
    fallbackChains: {
      'design_system': 'design_system_simple',
      'testing': 'testing_basic',
      'documentation': 'documentation_minimal'
    }
  }
};

// Execution
const orchestrator = new ChainOrchestrator(orchestrationConfig);
try {
  const result = await orchestrator.execute();
  
  // Validate results
  const validation = await validateChainResults(result);
  if (!validation.success) {
    // Apply automatic fixes
    const fixes = await generateAutoFixes(validation.issues);
    await applyFixes(fixes);
  }
  
} catch (error) {
  // Handle orchestration errors
  const recovery = await handleOrchestrationError(error);
  if (recovery.canRecover) {
    await orchestrator.resume(recovery.checkpoint);
  }
}
```

## 3. Error Recovery Patterns

### 1. Prop Type Mismatches
```typescript
// Automatic prop type adaptation
const PropAdapter = {
  adaptValue(value: any, targetType: string): any {
    switch (targetType) {
      case 'enum':
        return this.adaptEnum(value);
      case 'union':
        return this.adaptUnion(value);
      case 'function':
        return this.adaptFunction(value);
      default:
        return value;
    }
  },
  
  adaptEnum(value: string): string {
    const enumMap = {
      'contained': 'solid',
      'outlined': 'outline',
      'text': 'ghost'
    };
    return enumMap[value] || value;
  }
};
```

### 2. Style Conflicts
```typescript
// Style conflict resolution
const StyleResolver = {
  resolveConflict(
    legacy: string,
    modern: string
  ): string {
    const merged = this.mergeStyles(legacy, modern);
    const optimized = this.optimizeStyles(merged);
    return this.validateStyles(optimized);
  },
  
  mergeStyles(a: string, b: string): string {
    // Merge logic
    return merged;
  }
};
```

### 3. Accessibility Issues
```typescript
// Accessibility recovery
const A11yRecovery = {
  async fixAccessibility(
    component: Component,
    issues: A11yIssue[]
  ): Promise<Component> {
    const fixes = await Promise.all(
      issues.map(issue => this.generateFix(issue))
    );
    return this.applyFixes(component, fixes);
  },
  
  async generateFix(issue: A11yIssue): Promise<A11yFix> {
    switch (issue.type) {
      case 'missing-aria':
        return this.generateAriaFix(issue);
      case 'contrast':
        return this.generateContrastFix(issue);
      case 'keyboard':
        return this.generateKeyboardFix(issue);
    }
  }
};
```

## 4. Chain Composition

### Scenario
Creating a complex chain from simpler chains.

```typescript
const CompositeChain = {
  async execute(input: any): Promise<any> {
    // Setup monitoring
    const monitor = new PerformanceMonitor();
    monitor.start();
    
    try {
      // Execute chains
      const result1 = await chain1.execute(input);
      monitor.checkpoint('chain1');
      
      const result2 = await chain2.execute(result1);
      monitor.checkpoint('chain2');
      
      const result3 = await chain3.execute(result2);
      monitor.checkpoint('chain3');
      
      // Validate results
      const validation = await this.validate([
        result1,
        result2,
        result3
      ]);
      
      if (!validation.valid) {
        throw new ChainValidationError(validation.errors);
      }
      
      return result3;
      
    } catch (error) {
      // Handle errors
      const recovery = await this.recover(error);
      if (recovery.success) {
        return recovery.result;
      }
      throw error;
      
    } finally {
      // Stop monitoring
      monitor.stop();
      await monitor.report();
    }
  },
  
  async recover(error: Error): Promise<Recovery> {
    const strategy = await this.selectRecoveryStrategy(error);
    return strategy.execute();
  }
};
```

## Best Practices

1. **Always Use Error Boundaries**
   ```typescript
   class ChainErrorBoundary extends React.Component {
     componentDidCatch(error: Error, info: React.ErrorInfo) {
       // Log error
       errorLogger.log(error, info);
       
       // Attempt recovery
       this.attemptRecovery(error);
     }
     
     async attemptRecovery(error: Error) {
       const recovery = await RecoverySystem.recover(error);
       if (recovery.success) {
         this.setState({ recovered: true });
       }
     }
   }
   ```

2. **Implement Fallback Chains**
   ```typescript
   const FallbackChain = {
     async execute(input: any): Promise<any> {
       try {
         return await primaryChain.execute(input);
       } catch (error) {
         return await this.fallback(input, error);
       }
     },
     
     async fallback(input: any, error: Error): Promise<any> {
       const fallbackConfig = await this.getFallbackConfig(error);
       return await fallbackChain.execute(input, fallbackConfig);
     }
   };
   ```

3. **Use Monitoring and Analytics**
   ```typescript
   const ChainMonitor = {
     async track(chain: Chain): Promise<void> {
       const metrics = await this.collectMetrics(chain);
       await this.analyze(metrics);
       await this.report(metrics);
     },
     
     async analyze(metrics: Metrics): Promise<Analysis> {
       return await AnalyticsEngine.analyze(metrics);
     }
   };
   ```

These examples demonstrate comprehensive error handling, chain composition, and recovery strategies for real-world scenarios. 