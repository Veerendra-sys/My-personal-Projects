Great question! Here are all **6 techniques** and exactly how to trigger each one with your hand in front of the webcam:

---

### 👆 1. Red — Reverse Cursed Technique
**Gesture:** Point your **index finger up only**, middle finger curled down
Red spiral arms spin outward from a bright core

---

### ✌️ 2. Void — Infinite Void
**Gesture:** Hold up **index + middle finger** (peace sign), ring & pinky down
Cyan geometric rings expand into infinite space

---

### 👌 3. Purple — Hollow Purple
**Gesture:** **Pinch** your index finger and thumb together (< 4cm apart on screen)
Strongest bloom — purple sphere explosion scatters particles everywhere

---

### 🖐 4. Shrine — Malevolent Shrine
**Gesture:** All **5 fingers spread open** (open palm facing camera)
Red slash lines + ground particles + upright domain shape

---

### 🤙 5. Blue — Lapse: Blue
**Gesture:** **Thumb up** with all other fingers curled (thumbs up)
Deep blue reverse spiral converging inward

---

### ✊ 6. Black Flash — 黒閃
**Gesture:** Make a **fist** (all fingers curled, none extended)
Triple screen flash + giant 黒閃 kanji appears + dark particle burst

---

### Quick Checklist to Verify All 6 Work
Try them in this order in good lighting:

1. ✊ Fist → should say **Black Flash**
2. 🖐 Open palm → should say **Malevolent Shrine**
3. ✌ Peace sign → should say **Infinite Void**
4. 👆 Index only → should say **Red**
5. 🤙 Thumbs up → should say **Blue**
6. 👌 Pinch → should say **Hollow Purple**

The **gesture guide at the bottom of the screen** also highlights the active technique in its color when detected — that's the easiest way to confirm all 6 are working live.

What Was Built & Changed
Technologies Used
1. Three.js (3D Graphics Library)
The entire particle system — the swirling cursed energy effects, spirals, domain shapes — is built with Three.js. It handles the 3D scene, camera, and rendering. The EffectComposer + UnrealBloomPass add the glowing bloom effect that makes particles look like they're radiating light.
2. MediaPipe Hands (AI Hand Tracking)
Google's MediaPipe library runs a real-time AI model through your webcam to detect 21 hand landmarks (fingertip positions, knuckle joints, etc.). The gesture detection logic reads those landmark coordinates to figure out which technique you're activating — pinch distance, which fingers are extended, etc.
3. WebGL (via Three.js)
Three.js uses WebGL under the hood to render 25,000+ particles on the GPU simultaneously. Without WebGL this would be impossibly slow.
4. CSS Animations & Custom Properties
The UI — letterboxing, flash cards, energy meter, waveform bars, corner brackets — is all pure CSS with @keyframes animations, CSS custom properties (--accent, --accent-glow) that update dynamically when you switch techniques.
5. Google Fonts
Noto Serif JP for the Japanese title, Cinzel and Cinzel Decorative for the cinematic English labels — loaded via Google Fonts CDN.

Changes Made to the Original
AreaOriginalEnhancedTechniques4 (Red, Void, Purple, Shrine)6 (+ Blue, Black Flash)Particle count20,00025,000 + 5,000 ambient background layerParticle shapesBasic spirals/spheresAdded inner rings (Void), slash lines (Shrine), converging spiral (Blue), explosion burst (Black Flash)CameraStaticSlow 3D drift/parallaxUI layoutSimple centered textFull cinematic HUD — letterbox, energy meter, waveform, gesture guide, corner brackets, status stripTechnique activationText label change onlyFull-screen cinematic flash card with Japanese kanji, white flash, screen shakeBlack FlashDidn't existTriple screen flash + 黒閃 kanji overlay animationDomain atmosphereNonePer-technique colored radial gradient overlaysTypographyCourier NewNoto Serif JP + Cinzel DecorativeCSS variablesNoneDynamic --accent color swaps entire UI per technique