# Stage 1 – Basic Password Manager

## Objective
Build the core logic of a password manager using Python without focusing on security.

## Features Implemented
- Add a password for a website
- View stored passwords
- Password validation:
  - Minimum 8 characters
  - At least one digit
  - At least one special symbol
  - At least one uppercase letter
  - At least one lowercase letter
- Store passwords in a file for persistence

## Technical Details
- Language: Python
- Data stored in key:value format
- File name is `.json` but data is stored as plain text (not true JSON)

## Limitations
- Passwords are stored in plain text
- No master password
- No deletion functionality
- No encryption

## Reason for Limitations
Security-related features are intentionally skipped in this stage.
They will be implemented in Stage 2.

## Next Stage (Stage 2)
- Add master password authentication
- Improve security
- Implement delete password functionality
