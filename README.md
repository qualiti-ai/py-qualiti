# Qualiti.ai Python Tools and Package

[🔗 Qualiti.ai](https://qualiti.ai) is a very powerful paid platform. However, this repo is called `qualiti` and is a free, open-source Python Package and Command Line Interface (CLI).

> This package provides easy-to-use tools that can benefit developers and testers! Just take a look below to see what's available.

- [Installation](#installation)
- Tools
  - [Configuration](#configuration)
  - [Attributer](#attributer)

## Installation

1. Install `qualiti` with your favorite package manager:

    ```bash
    pip install qualiti
    ```

2. Set your `OPENAI_API_KEY` Environment Variable. You can use the `qualiti set-env` command:

    ```bash
    qualiti conf set-env OPENAI_API_KEY <your-api-key>
    ```

3. Then start using it

    ```bash
    qualiti --help
    ```

## Configuration

This tool allows you to Set and Get key-value pairs in your Environment Variables or the `qualiti.conf.json`.

> 💡 This is shown in Step 2 of the [Installation](#installation) section

### Usage

```bash
qualiti conf [COMMAND] [OPTIONS]
```

### Examples

This is helpful if you know that your elements are in specific files. This makes tools like [Attributer](#attributer) faster and cheaper since the AI will only look at files that you care about.

For example, in Angular, you may know that your HTML only exists in these file patters:

- `*.component.ts`
- `*.component.html`

We can set the `GLOB_PATTERN` value to only look for component files.

```bash
qualiti conf set-conf GLOB_PATTERN "*.component.*"
```

## Attributer

---

Use AI to auto-add `data-testid` attributes to HTML code.

### 🤖 Usage

```bash
qualiti attr testid [PATH] [OPTIONS]
```

> 💡 You can enter a path to a single file or to a directory.

If `PATH` is a directory, it will recursively look for *__all supported files__* in that directory and its subdirectories.

See [qualiti.conf.json](./qualiti/qualiti.conf.json) for the supported file types 👀

```bash
# file
qualiti attr testid examples/StoreView.tsx

# directory
qualiti attr testid examples/SubComponents
```

### 🤕 Problem

Although it's "best practice" for Web Pages to have dedicated attributes for Test Automation and Accessibility (a11y), it seems to be an afterthought and is not commonly followed.

- ❌ This makes the website *__inaccessible__* for a large group of people (ie screen readers, keyboard navigation)
- ❌ This makes it difficult to design and create Test Automation for the UI (ie component, end-to-end)

Ideally, developers would design their UI and components with these attributes in mind *__as they code__* since adding them is simple -- especially with a proper `Design System` -- but imagine a developer inheriting an existing project because they're a new hire, moving teams, or jumping into a project to help out. Spending the time and energy to do all of this manually isn't as simple:

1. Find the appropriate files (could be dozens or hundreds!)
2. Locate the relevant elements in each file
3. Add these attributes with helpful names for each element

### ✅ Solution

Using AI, we can do all 3 steps automatically!

1. They provide the file(s) like a `filename.tsx` or a folder like `/Components`
2. AI adds a `data-testid` to each relevant element
3. The new file is saved and can now be compared to the original in case the dev wants to make any changes

> 💡 Theoretically, this approach should work for any Web Framework like Angular, React, Vue, etc!

### 💭 Considerations

See [attributer.py](/qualiti/attributer.py) for the prompt and commands used.

- OpenAI ain't free, so be cognizant of how many files you target since each file will invoke the AI
- Use `git` so you get a diff before you push the updated files.
