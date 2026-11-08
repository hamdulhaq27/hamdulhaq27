<div align="center">

[[pic:hero/hero|Hamd Ul Haq — AI Engineer. Animated title cycles through: AI Engineer, Machine Learning Developer, Building Intelligent Systems, AI Automation Engineer, Exploring LLMs and Applied AI.|840]]

<br>

**AI undergraduate at FAST-NUCES Islamabad building LLM applications, voice and RAG assistants, automated data pipelines and deep-learning models — from data collection to deployment.**

<br>

[[btn:linkedin|https://linkedin.com/in/hamdulhaq/|LinkedIn]]&nbsp;
[[btn:github|https://github.com/hamdulhaq27|GitHub]]

</div>

<br>

[[pic:decorations/section-02|02 — About: Practical AI, built end to end|840]]

<table>
<tr>
<td width="56%" valign="top">

I'm Hamd, a third-year Artificial Intelligence undergraduate at **FAST-NUCES Islamabad**.

Most of what I build sits where models meet real systems: a local LLM assistant that takes restaurant bookings by text or voice, a pipeline that scrapes, segments and scores property listings every morning, and a queue-backed scraper that enriches business leads and runs scheduled outreach.

I like the unglamorous parts that make AI usable — extracting structured slots *before* the LLM sees a message, dedup keys that make reruns safe, subprocess pipelines that refuse to sync half-finished data, and evaluation suites that say whether any of it actually works.

</td>
<td width="44%" valign="top">

[[pic:decorations/label-focus|Focus|]]<br>
LLM applications, RAG and voice assistants, applied ML

[[pic:decorations/label-interests|Interests|]]<br>
Agentic AI, MLOps, computer vision

[[pic:decorations/label-approach|Approach|]]<br>
Data collection → model → API → deployment, with evaluation in between

[[pic:decorations/label-domains|Domains|]]<br>
NLP · deep learning · data pipelines · backend APIs

</td>
</tr>
</table>

<br>

[[pic:decorations/section-03|03 — Journey: Professional journey|840]]

[[pic:timeline/journey|Vertical timeline. 2023 to present: BS Artificial Intelligence, FAST-NUCES Islamabad. Deep learning: XDL-IDS CNN-Attention-GRU. LLM systems: La Bella Tavola assistant. ML in production: Zameen Intelligence Platform. Automation: Lead Scraping and Outreach. Now: agentic AI and applied LLM systems.|840]]

<br>

[[pic:decorations/section-04|04 — Capabilities: What I build|840]]

<table>
<tr>
<td width="50%" valign="top">

[[pic:capabilities/ml|01 AI & ML — Models that predict and detect|400]]

Deep-learning and classical models built around a real question: a CNN-Attention-GRU for CAN-bus intrusion detection, KMeans market segmentation and weighted lead scoring.

<code>TensorFlow</code> <code>Keras</code> <code>PyTorch</code> <code>scikit-learn</code> <code>SHAP</code>

</td>
<td width="50%" valign="top">

[[pic:capabilities/llm|02 LLM apps — Assistants, RAG and tool use|400]]

Assistants that stay on task: state machines and slot memory around local models, Chroma retrieval, tool calls into CRM and SQLite, and streamed responses.

<code>Ollama</code> <code>Qwen</code> <code>Chroma</code> <code>sentence-transformers</code> <code>LangChain</code>

</td>
</tr>
<tr>
<td width="50%" valign="top">

[[pic:capabilities/automation|03 Automation — Pipelines that run themselves|400]]

Jobs that run on a schedule or a queue: daily cron pipelines that commit data and trigger redeploys, and Celery tasks scheduled with `eta` and staggered countdowns.

<code>Celery</code> <code>Redis</code> <code>GitHub Actions</code> <code>Apify</code> <code>SMTP</code>

</td>
<td width="50%" valign="top">

[[pic:capabilities/backend|04 Backend — APIs, queues and streaming|400]]

FastAPI services that stay responsive: REST endpoints for dashboards, WebSocket token streaming, and servers that enqueue work and report task status instead of blocking.

<code>Python</code> <code>FastAPI</code> <code>WebSockets</code> <code>Docker</code> <code>Render</code>

</td>
</tr>
<tr>
<td width="50%" valign="top">

[[pic:capabilities/data|05 Data — Scraping, enrichment, cleaning|400]]

Getting messy web data into a usable shape: Selenium scraping, website and LinkedIn enrichment, E.164 phone normalisation, email validation and `place_id` dedupe.

<code>Selenium</code> <code>BeautifulSoup</code> <code>Pandas</code> <code>NumPy</code> <code>Sheets API</code>

</td>
<td width="50%" valign="top">

[[pic:capabilities/systems|06 Systems — Models wired into products|400]]

End-to-end systems where the model is one component: speech-to-text → LLM → text-to-speech loops, scored data behind live dashboards, and scrapers feeding outreach.

<code>Faster-Whisper</code> <code>Piper</code> <code>React</code> <code>TypeScript</code> <code>Vercel</code>

</td>
</tr>
</table>

<br>

[[pic:decorations/section-05|05 — Stack: Tech stack|840]]

[[pic:stack/01-languages|Languages: Python, TypeScript, JavaScript, C++, C#|840]]
[[pic:stack/02-ai|AI and machine learning: PyTorch, TensorFlow, Keras, scikit-learn, pandas, NumPy, OpenCV, SHAP|840]]
[[pic:stack/03-llms|LLMs and generative AI: Hugging Face, LangChain, Ollama, Qwen, SBERT, Whisper, Piper TTS|840]]
[[pic:stack/04-backend|Backend and APIs: FastAPI, WebSockets, Celery, REST|840]]
[[pic:stack/05-automation|Automation and integrations: Selenium, BeautifulSoup, Apify, Google Sheets API, SMTP, GitHub Actions|840]]
[[pic:stack/06-databases|Databases and vector stores: Redis, SQLite, Chroma|840]]
[[pic:stack/07-frontend|Frontend, DevOps and tools: Docker, Git, React, Vite, Tailwind, Vercel, Render, Google Colab|840]]

<br>

[[pic:decorations/section-06|06 — Projects: Featured projects|840]]

### Lead Scraping & Outreach Automation

<sub><b>AI AUTOMATION · DATA PIPELINE</b></sub>

[[pic:projects/lead-scraping|Illustration (not a screenshot) of the Lead Scraping and Outreach architecture: browser → FastAPI → Redis → Celery worker → Google Sheets, a five-stage scrape pipeline, and staggered email sends.|840]]

Building a B2B lead list by hand means searching Maps, visiting every website, hunting LinkedIn for decision-makers and tracking who has already been emailed. This system does it in the background: give it a business type and a location, and it scrapes Google Maps, enriches every business, syncs clean leads to Google Sheets and runs scheduled outreach.

- **Non-blocking by design** — FastAPI only enqueues jobs and returns a task ID; a Celery worker on Redis does the work while the UI polls `/api/task-status`.
- **Fail-closed pipeline** — five subprocess stages (Apify Maps actor → website crawl → LinkedIn / Facebook / Instagram / YouTube enrichment → cleaning → Sheets sync); if any stage exits non-zero, partial data never reaches the sheet.
- **Clean, deduplicated output** — phones normalised to E.164, personal vs role-based emails split, leads merged by `place_id`, top five decision-makers ranked CEO/Founder → C-suite → directors.
- **Safe scheduling** — scrapes and campaigns can be queued for an exact time with `apply_async(eta=…)`; campaigns fan out one send per lead at +0s, +30s, +60s… and write `email_status` back, so reruns never email anyone twice.

<code>Python</code> <code>FastAPI</code> <code>Celery</code> <code>Redis</code> <code>Apify</code> <code>Google Sheets API</code> <code>SMTP</code> <code>Docker</code>

[[btn:repo|https://github.com/hamdulhaq27/Leads-Scraping-and-Outreach-Automation|Repository]]

[[pic:decorations/divider|divider|840]]

### Zameen Intelligence Platform

<sub><b>ML PIPELINE · LIVE PRODUCT</b></sub>

[[pic:projects/zameen-dashboard|Screenshot of the live Zameen Intelligence lead dashboard with KPI cards, top locations by volume, market segment distribution and highest-scored leads.|840]]

New real-estate leads in Karachi are scattered across thousands of listings, with no quick way to tell which are worth a call. Every morning at 7 AM PKT, this platform collects the day's flat listings from Zameen.com, segments the market, scores every lead and redeploys a live API and dashboard — with no manual step.

- **Automated daily run** — a GitHub Actions cron job scrapes, cleans, segments and scores, commits fresh CSVs, then triggers a Render redeploy.
- **Today-only scraper** — Selenium keeps only listings posted today and visits agency profiles for phone, email and listing counts.
- **Scoring and segmentation** — a weighted 0–100 lead score (price, area, price/sqft, recency, verified agency …) and KMeans (K = 4) tiers from Budget to Luxury.
- **Product surface** — FastAPI REST API in Docker on Render, single-file dashboard on Vercel with KPIs, trends, segments and filterable leads.

<code>Python</code> <code>Selenium</code> <code>BeautifulSoup</code> <code>Pandas</code> <code>scikit-learn</code> <code>FastAPI</code> <code>Docker</code> <code>GitHub Actions</code> <code>Render</code> <code>Vercel</code>

[[btn:repo|https://github.com/hamdulhaq27/B2B-Lead-Intelligence-Platform|Repository]]&nbsp;
[[btn:demo|https://b2-b-lead-intelligence-platform.vercel.app/|Live demo]]

[[pic:decorations/divider|divider|840]]

### La Bella Tavola — Conversational Reservation Assistant

<sub><b>LLM · RAG · VOICE AI</b> &nbsp;·&nbsp; team project, CS 4063 Natural Language Processing</sub>

[[pic:projects/la-bella-tavola|Illustration (not a screenshot) of the La Bella Tavola pipeline: chat and voice input, Faster-Whisper, slot extraction and FSM, prompt builder, Qwen via Ollama, Chroma RAG with tools, Piper TTS, and token streaming to a React UI.|840]]

Small LLMs running on a CPU drift, hallucinate and forget booking details halfway through a conversation. This fully local front-desk assistant handles reservations, changes, cancellations and menu, weather and helpdesk questions — by text or voice — by putting structure around the model instead of trusting it.

- **Structure before generation** — regex slot extraction and intent detection run first; a finite-state machine (`collecting → confirming → confirmed → modifying`) decides what is still missing.
- **Constrained local inference** — stage-specific prompts with few-shot examples, Qwen 1.8B / Qwen 2.5 3B Instruct via Ollama, `MAX_TOKENS = 250` and stop sequences, streamed token-by-token over FastAPI WebSockets to a React UI.
- **Voice loop** — Faster-Whisper speech-to-text in, Piper text-to-speech out as Base64 WAV.
- **RAG, tools and evals** — Chroma + sentence-transformers retrieval and tool calls (CRM, menu, weather, SQLite), plus an evaluation suite covering task completion, retrieval precision/recall/MRR, tool-call accuracy and latency (TTFT, p90, p99).

<code>Python</code> <code>FastAPI</code> <code>WebSockets</code> <code>Ollama</code> <code>Qwen</code> <code>Chroma</code> <code>sentence-transformers</code> <code>Faster-Whisper</code> <code>Piper</code> <code>React</code> <code>TypeScript</code> <code>Docker Compose</code>

[[btn:repo|https://github.com/hamdulhaq27/Conversational-AI|Repository]]

[[pic:decorations/divider|divider|840]]

### XDL-IDS — CNN-Attention-GRU Intrusion Detection

<sub><b>DEEP LEARNING · SECURITY</b> &nbsp;·&nbsp; team project, AI-3003 Artificial Neural Networks</sub>

[[pic:projects/xdl-ids|Illustration (not a screenshot) of the CNN-Attention-GRU model: CAN bus frames through Conv1D, multi-head self-attention, GRU and dense layers to Normal, DoS or Spoofing, with reported results.|840]]

A car's CAN bus has no built-in authentication, so spoofing and denial-of-service attacks have to be spotted from message patterns alone. This project extends the published XDL-IDS CNN-GRU detector by inserting a multi-head self-attention layer, then stress-tests generalisation by merging two datasets.

- **Architecture** — Input → Conv1D → multi-head self-attention → GRU → Dense, compared against the CNN-GRU baseline.
- **Dataset expansion** — CICIoV2024 merged with the Car Hacking dataset: hex payloads to decimal, a unified `ID, DATA_0–DATA_7` schema and cross-dataset attack-label mapping.
- **Efficient training** — mixed precision (float16), XLA JIT and larger batches on a Colab T4.
- **Reported results** — 100% binary accuracy on CICIoV2024 (baseline ~99.9%) with faster convergence; on the harder merged dataset ~93–94% binary and ~75% multiclass. SHAP ranks `DATA_0` and `DATA_1` as the most important features.

<code>Python</code> <code>TensorFlow</code> <code>Keras</code> <code>scikit-learn</code> <code>SHAP</code> <code>Google Colab</code>

[[btn:repo|https://github.com/hamdulhaq27/CNN-GRU-IDS-Reproduction|Repository]]

<br>

[[pic:decorations/section-07|07 — Analytics: GitHub analytics|840]]

[[pic:analytics/languages|Most used languages by lines of code across 7 public repositories: Python 54.8%, TypeScript 33.5%, HTML 4.4%, C# 3.5%, CSS 2.2%, JavaScript 1.1%, PowerShell 0.5%.|840]]

<div align="center">

[[ext:streak|Contribution streak for hamdulhaq27]]

</div>

<br>

[[pic:decorations/section-08|08 — Process: Engineering process|840]]

[[pic:process/engineering-workflow|Six-stage engineering process: 01 Understand — find the real problem, users, data and constraints. 02 Architect — design the system, data flow and integrations. 03 Build — develop the backend, automation and AI layer. 04 Integrate — connect models, tools, APIs, databases and services. 05 Test and optimize — validate reliability, performance and usability. 06 Deploy — ship a maintainable, working solution.|840]]

<br>

[[pic:decorations/section-09|09 — Focus: Currently exploring|840]]

<table>
<tr>
<td width="33%" valign="top">

[[pic:focus/agentic|A — Agentic AI architectures|280]]

Agents that plan, call tools and recover when a step fails — a natural next step from the tool-calling and state-machine design in La Bella Tavola.

</td>
<td width="33%" valign="top">

[[pic:focus/voice|B — Voice and conversational AI|280]]

Faster speech pipelines and better grounding for small, local models, so voice assistants stay quick and accurate on modest hardware.

</td>
<td width="33%" valign="top">

[[pic:focus/mlops|C — MLOps and production ML|280]]

Scheduling, monitoring and redeploying models reliably — the discipline behind keeping a daily pipeline like Zameen's healthy.

</td>
</tr>
</table>

<br>

[[pic:decorations/section-10|10 — Connect|840]]

[[pic:decorations/connect|Open to collaboration — collaborations and conversations about applied AI, LLM systems and automation are always welcome.|840]]

<div align="center">

<br>

[[btn:linkedin|https://linkedin.com/in/hamdulhaq/|LinkedIn]]&nbsp;
[[btn:github|https://github.com/hamdulhaq27|GitHub]]

<br><br>

<sub>Designed and built from data to deployment · Machine Learning · NLP · Computer Vision · MLOps · Agentic AI</sub>

</div>
