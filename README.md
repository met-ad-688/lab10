# Module 5 Lab 2: Supervised Classification Methods over Big Data

Course source: [AD688-Web-Analytics/M5/M05_Lab02.qmd](https://github.com/BostonAnalytics/AD688-Web-Analytics/blob/main/M5/M05_Lab02.qmd). Follow that handout for the full tasks, questions, and grading requirements.

Starter file: `M05-lab02-your-bu-username.qmd`. Replace `your-bu-username` in the filename with your BU username and replace the author placeholder with your name. Keep `_system_code/` beside the source file.

## Environment

Use your assigned AWS EC2 environment and VS Code Remote SSH, as required by the course handout. Run the commands below from this repository's root. Reuse `.venv` if it already exists.

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install pandas numpy scikit-learn matplotlib seaborn plotly pyspark gdown tqdm jupyter xhtml2pdf nbconvert jupyterlab pyarrow polars kaleido fastparquet openpyxl lxml beautifulsoup4 requests quarto quarto-cli wheel psutil
```

Use the Quarto CLI installed during the course setup. Verify it with `quarto --version`. For PDF output, install a TeX distribution if one is not already available:

```bash
quarto install tinytex
```

After installing the packages needed for your work, record the environment with `python -m pip freeze > requirements.txt`.

## API and workbook setup

Copy `.env.example` to `.env` and enter your existing API key. Request a key only if you do not already have one, through the [MET API key request page](https://met-employability-services.azurewebsites.net/api/request-key/).

```bash
cp .env.example .env
```

The activity code in this repository is `M05_Lab02`:

```text
EMPLOYABILITY_API_KEY=replace_with_your_student_api_key
EMPLOYABILITY_API_BASE_URL=https://met-employability-services.azurewebsites.net
EMPLOYABILITY_API_PATH_PREFIX=/met-career-match
RESEARCH_ASSIGNMENT_CODE=M05_Lab02
```

Preserve an existing `.env` rather than overwriting it; update its activity code manually. Set `RESEARCH_SEMESTER_CODE` only if your instructor supplies a semester code.

The lab handout controls whether API access is needed. The template keeps workbook creation and validation disabled by default; enable them only if your instructor requests a research workbook. Lab 1 of Module 1 needs an API key for ingestion; Lab 2 of Module 1 reads Parquet and does not need an API key for its data tasks.

Matching student/question deliveries reuse an existing workbook in `research_submissions/`. Changed deliveries create a new timestamped workbook while preserving the previous one. Use the newly generated workbook after an activity-code change. The `_current_workbook.txt` file is a pointer, not an Excel workbook.

## Course data

Reuse the shared dataset folder beside this repository. Download it only if it is missing:

[Download the course data from Google Drive](https://drive.google.com/drive/folders/1Tq5Uixwz5J-aG_NfUQdI6X9CIrNz9ZFS?usp=drive_link)

```bash
gdown --folder "https://drive.google.com/drive/folders/1Tq5Uixwz5J-aG_NfUQdI6X9CIrNz9ZFS?usp=drive_link" -O ../Jobs_2026
```

Keep raw data outside Git. The shared `_system_code.paths.resolve_jobs_data_dir()` helper locates `../Jobs_2026` on EC2; set `JOBS_DATA_DIR` explicitly when using a different location. For the two-dataset ingestion lab, use `JOBS_2026_DIR` and `JOBS_2026_US_DIR` as described in its handout. Follow the handout's sample/full-data controls and row limits.

## Render your work

Run your analysis cells in order in the assigned environment and save the source. For `.qmd` analysis cells to execute during rendering, use `eval: true` at document or cell level. The optional workbook validation cell remains disabled until you finish the workbook. Keep the System Check cell enabled and its output visible, especially for Assignment 1.

After renaming the starter, substitute your actual filename below. Render each format in sequence:

```bash
quarto render M05-lab02-your-bu-username.qmd --to html
quarto render M05-lab02-your-bu-username.qmd --to docx
quarto render M05-lab02-your-bu-username.qmd --to pdf
```

If working in Jupyter, save an executed `.ipynb` and use the same render commands with that extension. Conversion between source formats is optional:

```bash
quarto convert M05-lab02-your-bu-username.ipynb
quarto convert M05-lab02-your-bu-username.qmd
```

Inspect the HTML, Word, and PDF outputs for visible results, readable tables, figures, and missing dependencies. HTML supports interactive figures; include static figures suitable for Word/PDF. Render only the formats required below for submission. Keep the `.qmd` or `.ipynb` source in Git.

## Submission and retained work

This lab is self-paced and formative. No submission is required. Keep the completed code and `_output` files in your GitHub repository for reference.

## AI disclosure and repository hygiene

Keep a separate AI disclosure document recording each tool/provider, date, task, complete prompts, shared conversation links where supported, relevant outputs, validation steps, and corrections. Assignments require the separate disclosure; labs follow the handout's submission policy.

Commit meaningful progress regularly. Keep `.env`, API keys, `.venv/`, raw datasets, and private research workbooks/reports out of Git. Review rendered output before sharing it. `_system_code/` must be committed so the template remains portable.
