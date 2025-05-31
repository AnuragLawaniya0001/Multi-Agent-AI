# 🤖 Multi-Agent AI System

A modular AI system designed for intelligent content routing and transformation using LLM-based agents. The system classifies inputs and processes them via specialized downstream agents including JSON Agent and Email Agent.

---

##  Table of Contents

- [Overview](#-overview)
- [Architecture](#-architecture)
- [Features](#-features)
- [Agents](#-agents)
  - [Classifier Agent](#classifier-agent)
  - [JSON Agent](#json-agent)
  - [Email Agent](#email-agent)

---

##  Overview

This project demonstrates a scalable and extensible approach to multi-agent AI architecture. It includes:

- LLM-powered intent and format detection
- Modular agent routing
- Robust logging and extensibility
- Support for structured and unstructured input

---

##  Architecture

            +------------+
            |   Input    |
            +------------+
                 |
                 v
         +------------------+
         | Classifier Agent |
         +------------------+
            /         \
           /           \
  | JSON Agent |       | Email Agent |
  
                  \ /
                  \ /
            +--------------+
            | Final Output |
            +--------------+

##  Features

- LLM-based classifier for routing
- Schema validation and normalization for JSON
- Email parsing with CRM-ready extraction
- Clean, structured logging system
- Easily extendable to new agents


## Agents

 **Classifier Agent**: Detects intent and content format using LLM.
 **JSON Agent**: Validates and reformats structured JSON inputs.
 **Email Agent**: Extracts metadata and CRM-ready fields from emails.

