---
name: make-a-simple-chart
domain: digital
locale: [generic]
interface: mixed
difficulty: basic
est_time: 5min
risk: low
prerequisites: []
status: draft
last_verified: 2026-08-17
---

## Goal

Create a basic chart from labeled spreadsheet data.

## Preconditions

- The data has labels in one column or row and numeric values in another.
- The data range has no fully blank rows inside it.

## Steps

1. **Select the chart data.** Drag across the labels and numbers, including headers if present. → *Expect:* the intended data range is highlighted.
2. **Insert a chart.** [BRANCH: Excel | Google Sheets] Excel: choose `Insert > Recommended Charts` or a chart type; Google Sheets: choose `Insert > Chart`. → *Expect:* a chart appears on or near the sheet.
3. **Choose the chart type.** Pick a column, bar, line, or pie chart that matches the data. → *Expect:* the chart updates to the selected type.
4. **Set the title.** Click the chart title or use chart settings to enter a clear title. → *Expect:* the chart title describes what the numbers show.
5. **Check the axes or legend.** Confirm labels and values are assigned correctly. → *Expect:* category labels and numeric scale or legend match the selected data.

## Decision points

- Comparing categories → use a bar or column chart.
- Showing change over time → use a line chart.
- Showing parts of one whole → use a pie chart only when categories are few and values sum to one total.

## Failure modes & recovery

- **F1 Wrong data range:** detect missing or extra values in the chart → edit the chart data range and select the correct cells.
- **F2 Labels treated as values:** detect category names plotted as a series → enable header or label options in chart setup.
- **F3 Chart unreadable:** detect crowded labels → switch chart type, filter data, or widen the chart.

## Verification

The chart is visible, uses the intended data range, has a descriptive title, and displays the selected labels and numeric values correctly.

## Variations

- `excel`: Use `Chart Design > Select Data` to repair the source range.
- `google-sheets`: Use the Chart editor `Setup` tab to change chart type and data range.

## Safety & privacy

Low risk. Charts may make hidden or sensitive data easier to notice, so remove private series before sharing.
