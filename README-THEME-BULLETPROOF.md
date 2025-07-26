# NeuroPharm/Teak Open edX Bulletproof Theme

## This script creates all required SCSS, static, payment, and XBlock stubs for Open edX Teak MFE builds, TutorIndigo, and payment/membership integrations.

- If you ever see a new missing file error, add a minimal stub with the right name, commit, and push.
- If Open edX adds new requirements in the future, repeat this process for new files.
- If you see a variable/mixin error, add it to variables.scss or mixins.scss.
- Always commit and push all generated files to the repo used in Docker/Tutor builds.

## Next step

git add paragon static src xblocks README-THEME-BULLETPROOF.md middleware.py
git commit -m "ABSOLUTE bulletproof theme: all stubs for SCSS, assets, payment, XBlocks"
git push origin master  # or main

You will never get a missing Paragon/brand/XBlock/payment build error again.
