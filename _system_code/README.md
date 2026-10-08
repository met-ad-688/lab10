# Shared course helpers

Keep `_system_code/` at the repository root beside the starter document.

- `research_survey.py` and `research_survey_workbook.py` are synchronized from `met-employability-services/analytics/_system_code/`. They support semester-aware API requests, student/delivery-specific workbook reuse, and local validation. Changed survey deliveries create a fresh workbook while preserving the previous file.
- `paths.py` and `__init__.py` are synchronized from `AD688-Web-Analytics/_system_code/`. `resolve_jobs_data_dir()` honors `JOBS_DATA_DIR` and locates the shared dataset on EC2.

Set the current activity's `RESEARCH_ASSIGNMENT_CODE` in the private `.env` file; see the repository README. The generic helper default is `M01_A`, so use this repository's `.env.example` when setting up another activity. `RESEARCH_SEMESTER_CODE` is optional and should only be set to a value provided by the instructor.

Run from the repository root. `prepare_workbook()` contacts the API and creates or reuses an Excel workbook. `validate_workbook()` checks it locally and writes a JSON report; it does not submit responses. The current-workbook `.txt` file is only a pointer, not the workbook. Do not commit generated research responses or credentials.
