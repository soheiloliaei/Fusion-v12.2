# 🎯 Fusion V12.2 UX Examples

Detailed examples of agent responses following the UX protocol for the Figma-to-prototype chain.

## 🔄 Complete Chain Example

### Input
```json
{
  "request": "Convert this Figma design into a working prototype",
  "mcp_json": {
    "components": [
      {
        "name": "PrimaryButton",
        "variants": ["default", "hover", "disabled"],
        "properties": {
          "padding": "16px",
          "borderRadius": "8px"
        }
      }
    ]
  }
}
```

### 1. ComponentLibrarian Response

✅ Context confirmed. Extracting token + variant structure.

```json
{
  "tokens_extracted": {
    "components": 1,
    "variants": 3,
    "properties": 2
  },
  "metrics": {
    "token_fidelity": 0.92,
    "pattern_effectiveness": 0.88,
    "confidence_score": 0.90,
    "clarity_score": 0.91
  }
}
```

Here is the extracted token map:
- Component: PrimaryButton
- Variants: default, hover, disabled
- Core properties identified and normalized

### 2. DesignTechnologist Response

✅ Analyzing component structure for React implementation.

```typescript
interface PrimaryButtonProps {
  variant?: 'default' | 'hover' | 'disabled';
  children: React.ReactNode;
}

export const PrimaryButton: React.FC<PrimaryButtonProps> = ({
  variant = 'default',
  children
}) => {
  const baseStyles = 'px-4 py-2 rounded-lg';
  const variantStyles = {
    default: 'bg-blue-500 text-white',
    hover: 'bg-blue-600 text-white',
    disabled: 'bg-gray-300 text-gray-500'
  };
  
  return (
    <button 
      className={`${baseStyles} ${variantStyles[variant]}`}
      disabled={variant === 'disabled'}
    >
      {children}
    </button>
  );
};
```

```json
{
  "metrics": {
    "buildability_score": 0.93,
    "token_fidelity": 0.91,
    "confidence_score": 0.89,
    "clarity_score": 0.90
  }
}
```

### 3. PromptEngineer Response

✅ Creating prompt scaffold for component generation.

I've structured the following prompt patterns:
1. Token extraction and normalization
2. Component structure definition
3. Variant handling logic
4. Accessibility requirements

```json
{
  "metrics": {
    "clarity_score": 0.92,
    "pattern_effectiveness": 0.89,
    "confidence_score": 0.88,
    "innovation_score": 0.87
  }
}
```

### 4. ProductNavigator Response

✅ Analyzing product context and JTBD alignment.

Key insights for the button component:
1. Primary action emphasis needed
2. Clear state transitions
3. Accessibility considerations
4. Mobile responsiveness

```json
{
  "metrics": {
    "innovation_score": 0.88,
    "actionability_score": 0.87,
    "confidence_score": 0.86,
    "clarity_score": 0.89
  }
}
```

### 5. VPOfDesign Response

✅ Reviewing design output against SLT standards.

The component implementation meets our quality bar with a few suggestions:
1. Rename variant 'disabled' to 'inactive' for clarity
2. Add aria-labels for accessibility
3. Include loading state variant

```json
{
  "metrics": {
    "clarity_score": 0.96,
    "narrative_cohesion": 0.92,
    "confidence_score": 0.94,
    "pattern_effectiveness": 0.93
  }
}
```

### 6. VPOfProduct Response

✅ Evaluating product strategy and delivery path.

Component is ready for implementation with:
1. Clear use cases defined
2. Technical requirements met
3. Accessibility standards addressed
4. Scalable variant system

```json
{
  "metrics": {
    "actionability_score": 0.91,
    "technical_feasibility": 0.89,
    "confidence_score": 0.90,
    "clarity_score": 0.92
  }
}
```

## ⚠️ Error Handling Examples

### Low Confidence Response
```json
{
  "confidence_score": 0.72,
  "response": "⚠️ Some aspects of the design token structure are unclear. Could you clarify:\n1. Button state transitions\n2. Color token relationships\n3. Spacing scale"
}
```

### Fallback Pattern Example
```json
{
  "pattern_effectiveness": 0.71,
  "response": "⚠️ Complex component structure detected. Switching to SignalExtractor pattern for better token analysis."
}
```

### Missing Mode Example
```json
{
  "response": "🧭 Please confirm the execution mode you'd like to use: simulate, ship, critique, or prototype?"
}
```

## 📊 Metrics Display Format

Every response includes:
```json
{
  "metrics": {
    "clarity_score": 0.xx,
    "confidence_score": 0.xx,
    "pattern_effectiveness": 0.xx,
    "innovation_score": 0.xx,
    "[additional_relevant_metrics]": 0.xx
  }
}
```

## 🎨 Style Guidelines

1. No em dashes used
2. Full sentences for main points
3. Bullet points only for lists
4. Clear hierarchy in responses
5. Emoji prefixes for status
6. Metrics always included
7. SLT-ready formatting when required 