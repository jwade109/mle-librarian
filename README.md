# Clark the MLE Librarian

## `!post`

Write a predefined series of formatted messages to a Discord text channel.

__WARNING: This will erase _all_ messages authored by `@MLE Librarian`
in the target channel.__

To post a named file: `!post #target-channel [file.yml]`

To post an uploaded file: `!post #target-channel` (with attached file)

The following criteria must be met to `!post`:

- The target channel must be on the `!whitelist`
- The target channel must not contain messages authored by anyone but `@MLE Librarian`
- The command invoker must be on the `!staff`

Valid YAML (`.yml`) files look generally like this:

```yaml
- pinned: true
  body: "
  _ _

  **Q: Can I have a picture of a cute bird?**"

- attachments: ["https://i.imgur.com/JHbEXIM.jpg"]
  body: "
  ~

  A: Here you go!"
```

## `!whitelist`, `!blacklist`

Adds a text channel to the `!post` whitelist, allowing them to be `!post`ed to. Correspondingly, `!blacklist` removes channels from the whitelist.

To view the whitelist: `!whitelist`

To add a channel: `!whitelist #channel`

To remove: `!blacklist #channel`

## `!staff`, `!hire`, `!fire`

In order to be able to `!post`, a user must first be `!hire`d. Once hired,
they are a member of the staff.

To view all staff members, use `!staff`.

To add a user to the staff: `!hire @new_staff_member`

To remove a member from the staff: `!fire @new_staff_member`
