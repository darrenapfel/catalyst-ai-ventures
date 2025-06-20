#!/bin/bash

# Documentation Consistency Checker
# Purpose: Quickly identify potential inconsistencies after strategic changes

echo "=== Documentation Consistency Check ==="
echo "Date: $(date)"
echo ""

# Check for common inconsistencies
echo "1. Checking for outdated revenue targets..."
echo "Files mentioning '10M', 'ARR', or 'revenue target':"
grep -r "10M\|ARR\|revenue target" --include="*.md" . 2>/dev/null | grep -v "check-doc-consistency" | head -10
echo ""

echo "2. Checking for segment restrictions..."
echo "Files mentioning 'avoid', 'red flag segments', or customer restrictions:"
grep -r "avoid\|red flag\|students\|seniors\|nonprofits" --include="*.md" . 2>/dev/null | grep -v "check-doc-consistency" | head -10
echo ""

echo "3. Checking ROI focus adoption..."
echo "Files NOT mentioning ROI/LTV/CAC (may need updates):"
for file in $(find . -name "*.md" -type f | grep -E "(strategy|framework|evaluation)" | grep -v "node_modules"); do
    if ! grep -q "ROI\|LTV\|CAC\|unit economics" "$file" 2>/dev/null; then
        echo "  - $file"
    fi
done
echo ""

echo "4. Recently modified documentation (last 10):"
find . -name "*.md" -type f -exec ls -lt {} + 2>/dev/null | grep -v "node_modules" | head -10
echo ""

echo "5. Key documentation files by category:"
echo ""
echo "Strategy Documents:"
ls -la docs/strategy/*.md 2>/dev/null || echo "  No strategy docs found"
echo ""
echo "Framework Documents:"
ls -la docs/framework/*.md 2>/dev/null || echo "  No framework docs found"
echo ""
echo "Decision Records:"
ls -la decisions/*.md 2>/dev/null | tail -5 || echo "  No decision records found"
echo ""

echo "6. Checking for term consistency..."
echo "Different ways we refer to our approach:"
echo "  'ROI-focused': $(grep -r "ROI-focused" --include="*.md" . 2>/dev/null | wc -l) occurrences"
echo "  'industry-agnostic': $(grep -r "industry-agnostic" --include="*.md" . 2>/dev/null | wc -l) occurrences"
echo "  'profitability': $(grep -r "profitability" --include="*.md" . 2>/dev/null | wc -l) occurrences"
echo ""

echo "=== Check Complete ==="
echo "Review the documentation index at: docs/reference/documentation-index.md"
echo "For detailed impact mapping of changes"