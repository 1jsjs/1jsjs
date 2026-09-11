<p align="right"><strong>English</strong> &nbsp; / &nbsp; <a href="./README.ko.md">한국어</a></p>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./assets/hero-dark.svg" />
  <source media="(prefers-color-scheme: light)" srcset="./assets/hero-light.svg" />
  <img src="./assets/hero-light.svg" width="100%" alt="Jinsu Park. Web apps and macOS tools." />
</picture>

<br/>

Hi, I'm Jinsu. I build web apps and macOS tools. My recent work includes a trackpad launcher, speech coaching, and interfaces for reviewing video edits.

[Portfolio](https://parkjinsu-portfolio.vercel.app) &nbsp; / &nbsp; [Resume](https://parkjinsu-portfolio.vercel.app/cv) &nbsp; / &nbsp; [jinsu.build@gmail.com](mailto:jinsu.build@gmail.com)

I also contributed a [merged fix to Apple’s coremltools](https://github.com/apple/coremltools/pull/2736): correcting `layer_norm` beta shape validation and updating the regression test.

## Thumbstap

<a href="https://github.com/1jsjs/thumbstap"><img src="./assets/cutaway/thumbstap.png" width="100%" alt="Thumbstap illustration: an elliptical thumb contact connects a trackpad to gesture calibration and a frosted app grid." /></a>

Double-tap your thumb on the trackpad to open an app grid. I designed, built, and released this macOS app on my own.

The gesture detector uses the shape of the touch contact to distinguish a thumb from a fingertip. Calibration adjusts it for the user; the SwiftUI launcher provides search and app arrangement.

`Swift` `SwiftUI` `Homebrew` &nbsp; Open source, MIT

[Gesture detection](https://github.com/1jsjs/thumbstap/blob/178c9c6/Sources/Thumbstap/Thumbstap.swift) · [Calibration](https://github.com/1jsjs/thumbstap/blob/178c9c6/Sources/Thumbstap/Calibration.swift) · [App grid](https://github.com/1jsjs/thumbstap/blob/178c9c6/Sources/ThumbstapApp/AppGridView.swift) · [Install](https://github.com/1jsjs/thumbstap#install)

## Sobi Tribunal

<a href="https://github.com/1jsjs/sobi-tribunal"><img src="./assets/cutaway/sobi.png" width="100%" alt="Sobi Tribunal illustration: its pig judge and courtroom connect purchase evidence, questions, verdict rules, and an explanation." /></a>

A pig judge questions your purchases. You submit a photo, answer questions, and get a verdict to help you reflect on your spending.

We entered the hackathon as a team of five. I planned the product, set up the infrastructure, and wrote all of v1 and v2. Rules determine the verdict; an LLM writes the explanation.

`FastAPI` `SQLite` `Amazon Bedrock` `EC2 / S3`

Encouragement Award, Honam LLM Hackathon.

[Verdict logic](https://github.com/1jsjs/sobi-tribunal/blob/c25efc3/services/verdict_service.py) · [Model integration](https://github.com/1jsjs/sobi-tribunal/blob/c25efc3/services/llm_service.py) · [Project details](https://parkjinsu-portfolio.vercel.app/case-studies/sobi-tribunal)

## SpeakUp

<a href="https://github.com/eecczz/speech-coach"><img src="./assets/cutaway/speakup.png" width="100%" alt="SpeakUp illustration: speech and transcript segments connect to coaching feedback, a replay viewer, and MP4 export." /></a>

A speaking coach that connects feedback to the recording, so you can go back and hear the moment being discussed.

On this team of three, I built the STT/LLM integration and coaching engine. I also added report replay and MP4 export.

`Speech APIs` `LLM integration` `TypeScript`

Bronze Award, JBNU AI & SW Competition, software division.

[Coaching engine](https://github.com/eecczz/speech-coach/blob/007b080/apps/web/src/realtime-coaching.ts) · [Replay and export](https://github.com/eecczz/speech-coach/blob/007b080/apps/web/src/report-page.ts) · [Project details](https://parkjinsu-portfolio.vercel.app/case-studies/speakup)

## Vispresso

<a href="https://github.com/Me1e/jbnu_capstone_vispresso"><img src="./assets/cutaway/vispresso.png" width="100%" alt="Vispresso illustration: the source preview, selected clip, and trim timeline are separated into aligned interface layers." /></a>

A video-editing tool developed with Jeonju MBC. It lets an editor review and adjust AI-suggested clips.

I handled the frontend on a team of four. I built the source preview, timeline, and in/out editing controls used to check those suggestions.

`TypeScript` `Video interfaces` `Timeline editing`

Excellence Award, Software Capstone Design Competition.

[Review workbench](https://github.com/Me1e/jbnu_capstone_vispresso/blob/9a8ae50/src/components/job-space/segment-review-v2.tsx) · [Timeline controls](https://github.com/Me1e/jbnu_capstone_vispresso/blob/9a8ae50/src/lib/editor-timeline.ts) · [Project details](https://parkjinsu-portfolio.vercel.app/case-studies/vispresso)

<sub>The images are illustrations based on the projects’ interfaces and features. The source links show the implementation.</sub>

## Tools I use

Frontend: React, Next.js, TypeScript, SwiftUI<br/>
Backend: Python, FastAPI, Node.js, SQLite<br/>
AI APIs and deployment: OpenAI, Gemini, Amazon Bedrock, EC2, S3, Docker

<details>
<summary>What I'm learning now</summary>

I'm studying machine learning fundamentals, LLMs, and RAG at Furiosa AI Agent School. My practice code is in [furiosa-practice](https://github.com/1jsjs/furiosa-practice).

I'm a Jeonbuk National University student, currently on leave.

</details>

---

I'm looking for an internship in AI application development or full-stack engineering.

[Email me](mailto:jinsu.build@gmail.com) &nbsp; / &nbsp; [Download CV](https://parkjinsu-portfolio.vercel.app/cv.pdf)
