# SentinelVision 

### AI-Powered Visual Safety

> See threats sooner. Safer tomorrows.

SentinelVision is a prototype AI-powered visual safety system designed to analyze surveillance video and identify potentially dangerous situations.

The long-term vision is to integrate SentinelVision with real-time CCTV cameras and enable automated responses to help reduce theft, robbery, and other security incidents in supermarkets, medical shops, and other sensitive locations.

> **Prototype Status:**  
> The current version implements the web interface, video upload pipeline, Flask backend, JSON communication, and OpenCV-based video processing. AI-based threat detection and real-time CCTV integration are planned next.

---

## Project Vision

Traditional CCTV systems primarily act as passive recording systems.

SentinelVision aims to move from:

**Passive Recording → Proactive Visual Safety**

The system is intended to:

- Detect people and relevant objects
- Analyze movement and interactions
- Identify potentially suspicious activity
- Calculate a threat level
- Present analysis results through an intuitive dashboard
- Eventually support real-time CCTV monitoring
- Enable automated security responses in future versions

---

## Current Features

The current prototype supports:

- Video upload through a web interface
- Uploaded video storage
- JavaScript frontend ↔ Flask backend communication
- FormData-based video transfer
- Python backend processing
- OpenCV video processing
- Video metadata extraction
- Frame-by-frame video reading
- JSON-based communication between backend and frontend
- SentinelVision visual dashboard

### Current Processing Pipeline

```text
User
 ↓
Upload Video
 ↓
HTML / CSS
 ↓
JavaScript
 ↓
Flask API
 ↓
Save Uploaded Video
 ↓
OpenCV
 ↓
Read Video Frames
 ↓
Extract Video Information
 ↓
JSON Response
 ↓
JavaScript
 ↓
Display Result