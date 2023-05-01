# Attributer

Auto-add attributes to Web Dev code.

## 🤕 Problem

Although it's "best practice" for Web Pages to have dedicated attributes for Test Automation and Accessibility (a11y), it seems to be an afterthought and is not commonly followed.

- ❌ This makes the website *__inaccessible__* for a large group of people (ie screen readers, keyboard navigation)
- ❌ This makes it difficult to design and create Test Automation for the UI (ie component, end-to-end)

Ideally, developers would design their UI and components with these attributes in mind *__as they code__* since adding them is simple -- especially with a proper `Design System` -- but imagine a developer inheriting an existing project because they're a new hire, moving teams, or jumping into a project to help out. Spending the time and energy to do all of this manually isn't as simple:

1. Find the appropriate files (could be dozens or hundreds!)
2. Locate the relevant elements in each file
3. Add these attributes with helpful names for each element

## ✅ Solution

Using AI, we can do all 3 steps automatically!

1. They provide the file(s) like a `filename.tsx` or a folder like `/Components`
2. AI adds a `data-testid` to each relevant element
3. The new file is saved and can now be compared to the original in case the dev wants to make any changes

> 💡 Theoretically, this approach should work for any Web Framework like Angular, React, Vue, etc!
