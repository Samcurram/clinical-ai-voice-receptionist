# Clinical AI Voice Receptionist & Automated Appointment Booking System

An autonomous, multi-lingual AI voice agent and automation pipeline designed for outpatient dental and medical clinics to handle inbound and outbound appointment booking calls in real time.

---

## 🎯 Overview
This project automates clinic receptionist workflows by combining Large Language Models (LLMs), speech-to-text (STT), text-to-speech (TTS), and tool-calling toolchains. It seamlessly captures patient details (name, contact number, and requested time slot) and syncs directly with calendar and database systems.

---

## 🚀 Key Features
- **Real-Time Conversational AI:** Low-latency turn-taking powered by advanced LLM orchestration.
- **Multi-Lingual Voice Support:** Fluent in Hindi and English for localized patient interactions.
- **Structured Tool Calling:** Automatically extracts entities (Patient Name, Phone Number, Preferred Date/Time) using Pydantic and JSON mode.
- **Database & Calendar Integration:** Verifies slot availability and writes confirmed appointments directly to backend PostgreSQL / Google Calendar APIs.
- **Human-in-the-Loop Safeguards:** Gracefully escalates complex medical queries or rescheduling conflicts to human reception staff.

---

## 🛠️ Tech Stack
- **Language:** Python 3.10+ / Asyncio / Pydantic
- **AI & Orchestration:** OpenAI / Gemini API, LangChain / Agentic Toolkits
- **Voice Pipeline:** Whisper (STT) & ElevenLabs / Neural TTS
- **Backend & Integrations:** FastAPI, PostgreSQL, Redis, REST Webhooks
