# The Girl I Want to Be

An adult, choice-driven visual novel about identity, relationships,
and personal development.

Status: early prototype  
Version: 0.1.0  
Primary language: English  
Planned translation: German

## Development tools

- Ren'Py SDK 8.5.3
- Visual Studio Code
- Official Ren'Py Language extension
- Git for Windows
- Venice for visual asset generation
- GIMP for image editing

## Getting started

1. Install and extract the Ren'Py SDK.
2. Set the launcher's projects directory to the parent of this folder.
3. Select TheGirlIWantToBe.
4. Click Launch Project.

The SDK is installed separately and is not part of this repository.

## Project structure

- game/ — Runtime scripts, interface, images, audio, and translations.
- ArtSource/ — Original images, references, and editable artwork.
- Builds/ — Generated distributions; excluded from Git.
- docs/ — Design documents, character profiles, and development notes.

Additional folders are created as needed.

## Planned features

- One visual protagonist with three selectable backgrounds:
  Bookworm, Girl Next Door, and Social Butterfly.
- Background-specific starting attributes and relationship situations.
- Character progression and branching decisions.
- Three walkthrough modes: Off, Hints, and Full.
- Replay gallery.
- Separate distribution editions from one shared codebase.
- English source text with German localization.

## Coding conventions

- English identifiers and comments.
- UTF-8 encoding.
- Four spaces per indentation level; no tabs.
- snake_case for script filenames, variables, and functions.
- Chapter-prefixed story labels, such as ch01_arrival.
- Separate story scripts, game systems, data, and interface code.
- Use default for mutable saved state.
- Use define for fixed definitions.
- Use persistent for cross-playthrough unlocks and preferences.
- Keep displayed interface text translatable.
- Apply stat changes through shared functions.
- Keep walkthrough information consistent with actual choice effects.

## Before committing

- Review the changes.
- Run Ren'Py Lint after script changes.
- Test affected scenes and features.
- Check save, load, rollback, and new-game behavior when changing state.

## Assets and builds

Source artwork and documentation must be excluded from distributed
game packages through Ren'Py build rules.

Git ignore rules do not control package contents.

Configure Git LFS before committing large artwork or media files.

## License

All rights reserved. No license is granted for redistribution or reuse
of original project materials. Third-party assets remain subject to
their respective licenses.