# # FILE: server.py
# import uvicorn
# import socketio
# import numpy as np
# from fastapi import FastAPI
# from fastapi.middleware.cors import CORSMiddleware

# # 1. Initialize Server & Allow Mobile Connection
# app = FastAPI()
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"], # Critical for mobile access
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# # 2. Setup Real-Time Socket
# sio = socketio.AsyncServer(async_mode='asgi', cors_allowed_origins='*')
# socket_app = socketio.ASGIApp(sio, app)

# # 3. BEHAVIOR DETECTION LOGIC (The "AI" Part)
# # derived from UCI HAR and SisFall datasets
# def analyze_behavior(data):
#     try:
#         # Get raw accelerometer data
#         ax = float(data.get('x', 0))
#         ay = float(data.get('y', 0))
#         az = float(data.get('z', 0))

#         # Calculate Vector Magnitude (Total G-Force)
#         # Formula: √(x² + y² + z²)
#         total_force = np.sqrt(ax**2 + ay**2 + az**2)

#         # --- THRESHOLD LOGIC ---
#         # ~9.8  = Standing/Sitting (Normal Gravity)
#         # ~15.0 = Walking/Jogging
#         # >25.0 = Sudden Impact / Hard Fall / Car Crash
        
#         if total_force > 25.0:
#             return "CRITICAL"
#         elif total_force > 15.0:
#             return "RUNNING"
#         else:
#             return "NORMAL"
            
#     except Exception as e:
#         return "ERROR"

# # 4. Event Listeners
# @sio.event
# async def connect(sid, environ):
#     print(f"✅ User Connected: {sid}")

# @sio.event
# async def sensor_stream(sid, data):
#     # Analyze the incoming data stream
#     status = analyze_behavior(data)
    
#     # If danger is detected, command the phone to panic
#     if status == "CRITICAL":
#         print(f"⚠️ EMERGENCY: Sudden Crash Detected for {sid}!")
#         await sio.emit('trigger_sos_command', {'msg': 'Crash Detected! Initiating SOS...'}, room=sid)

# @sio.event
# async def disconnect(sid):
#     print(f"❌ User Disconnected: {sid}")
# def check_danger(data):
#     ax, ay, az = float(data['x']), float(data['y']), float(data['z'])
#     total_force = np.sqrt(ax**2 + ay**2 + az**2)

#     # DATASET THRESHOLDS:
#     FALL_THRESHOLD = 25.0  # (approx 2.5g) - Critical Impact
#     RUN_THRESHOLD = 18.0   # (approx 1.8g) - Heavy Running
    
#     if total_force > FALL_THRESHOLD:
#         return "CRASH DETECTED"
#     elif total_force > RUN_THRESHOLD:
#         return "RUNNING"
#     return "NORMAL"
# # ==========================================
# # 📍 JAIPUR LOCATION DATABASE (PYTHON VERSION)
# # ==========================================

# # 1. SAFE HAVENS
# safe_havens = [
#     {
#         "name": "Malviya Nagar Police Station",
#         "type": "Police",
#         "lat": 26.8549,
#         "lng": 75.8243,
#         "phone": "0141-2550300",
#         "address": "Near Calgiri Marg, Malviya Nagar"
#     },
#     {
#         "name": "Bajaj Nagar Police Thana",
#         "type": "Police",
#         "lat": 26.8700,
#         "lng": 75.7950,
#         "phone": "0141-2702222",
#         "address": "Tonk Road, Bajaj Nagar"
#     },
#     {
#         "name": "Gandhi Nagar Police Station",
#         "type": "Police",
#         "lat": 26.8845,
#         "lng": 75.8005,
#         "phone": "0141-2706363",
#         "address": "Gandhi Nagar Mod"
#     },
#     {
#         "name": "Fortis Escorts Hospital",
#         "type": "Hospital",
#         "lat": 26.8511,
#         "lng": 75.8044,
#         "phone": "0141-2547000",
#         "address": "JLN Marg, Malviya Nagar"
#     },
#     {
#         "name": "Jaipuria Hospital",
#         "type": "Hospital",
#         "lat": 26.8555,
#         "lng": 75.8044,
#         "phone": "0141-2551500",
#         "address": "Milap Nagar"
#     },
#     {
#         "name": "Eternal Heart Care (EHCC)",
#         "type": "Hospital",
#         "lat": 26.8520,
#         "lng": 75.8080,
#         "phone": "0141-2770000",
#         "address": "Jawahar Circle"
#     },
#     {
#         "name": "Apex Hospitals",
#         "type": "Hospital",
#         "lat": 26.8620,
#         "lng": 75.8190,
#         "phone": "0141-4101111",
#         "address": "Malviya Nagar Sector 4"
#     },
#     {
#         "name": "MNIT Main Gate Security",
#         "type": "Security",
#         "lat": 26.8640,
#         "lng": 75.8162,
#         "phone": "0141-2529000",
#         "address": "JLN Marg"
#     },
#     {
#         "name": "Gaurav Tower (GT) Guard Post",
#         "type": "Security",
#         "lat": 26.8552,
#         "lng": 75.8067,
#         "phone": "N/A",
#         "address": "Indra Place"
#     },
#     {
#         "name": "World Trade Park (WTP) Helpdesk",
#         "type": "Security",
#         "lat": 26.8534,
#         "lng": 75.8051,
#         "phone": "0141-2728888",
#         "address": "JLN Marg"
#     }
# ]

# # 2. HAZARD ZONES
# hazard_zones = [
#     {
#         "lat": 26.8610,
#         "lng": 75.8100,
#         "reason": "No Street Lights (Dark Alley)",
#         "radius": 60
#     },
#     {
#         "lat": 26.8590,
#         "lng": 75.8080,
#         "reason": "Construction Debris & Uneven Road",
#         "radius": 50
#     },
#     {
#         "lat": 26.8500,
#         "lng": 75.8000,
#         "reason": "Prone to Water Logging",
#         "radius": 100
#     },
#     {
#         "lat": 26.8650,
#         "lng": 75.8200,
#         "reason": "Isolated Area (High Theft Risk)",
#         "radius": 80
#     }
# ]
# import math

# def check_geo_danger(user_lat, user_lng):
#     """
#     Checks if the user is inside any known Hazard Zone.
#     Returns the reason if dangerous, else None.
#     """
#     if not user_lat or not user_lng:
#         return None

#     # Earth radius in meters
#     R = 6371000 

#     for zone in hazard_zones:
#         # Calculate distance (Simple Euclidean approximation for short distances)
#         # For production, use Haversine formula
#         d_lat = math.radians(zone["lat"] - user_lat)
#         d_lng = math.radians(zone["lng"] - user_lng)
        
#         a = math.sin(d_lat/2) * math.sin(d_lat/2) + \
#             math.cos(math.radians(user_lat)) * math.cos(math.radians(zone["lat"])) * \
#             math.sin(d_lng/2) * math.sin(d_lng/2)
            
#         c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
#         distance = R * c

#         if distance <= zone["radius"]:
#             return f"WARNING: You have entered a Hazard Zone! {zone['reason']}"
            
#     return None
# @sio.event
# async def sensor_data(sid, data):
#     # 1. Check Crash (Accelerometer)
#     crash_status = check_danger(data)
    
#     # 2. Check Location Danger (GPS) - Assuming data sends lat/lng too
#     geo_status = None
#     if 'lat' in data and 'lng' in data:
#         geo_status = check_geo_danger(data['lat'], data['lng'])

#     # --- TRIGGERS ---
    
#     # A. If Crash Detected
#     if crash_status == "CRASH DETECTED":
#         print(f"⚠️ CRASH DETECTED for User {sid}!")
#         await sio.emit('force_sos_trigger', {'msg': 'Crash Detected! Sending Help...'}, room=sid)

#     # B. If Hazard Zone Entered (New Feature)
#     elif geo_status:
#         print(f"⚠️ HAZARD ZONE: {geo_status}")
#         # Send a warning message to the user, not a full SOS
#         await sio.emit('force_warning', {'msg': geo_status}, room=sid)

# # 5. Run the App
# if __name__ == "__main__":
#     uvicorn.run(socket_app, host="192.168.38.1", port=5000)
import uvicorn
import socketio
import numpy as np
import math
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# 1. SETUP SERVER
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

sio = socketio.AsyncServer(async_mode='asgi', cors_allowed_origins='*')
socket_app = socketio.ASGIApp(sio, app)

# 2. DATASETS
# Hazard Zones (Dark Alleys, Construction, etc.)
hazard_zones = [
    {"lat": 26.8610, "lng": 75.8100, "reason": "No Street Lights (Dark Alley)", "radius": 60},
    {"lat": 26.8590, "lng": 75.8080, "reason": "Construction Debris", "radius": 50},
    {"lat": 26.8500, "lng": 75.8000, "reason": "Water Logging Area", "radius": 100},
    {"lat": 26.8650, "lng": 75.8200, "reason": "Isolated Area (High Risk)", "radius": 80}
]

# 3. HELPER FUNCTIONS
def check_crash(data):
    """Detects falls using accelerometer data"""
    try:
        ax, ay, az = float(data['x']), float(data['y']), float(data['z'])
        total_force = np.sqrt(ax**2 + ay**2 + az**2)
        
        # Thresholds: >25.0 is a crash/fall
        if total_force > 25.0:
            return "CRASH"
        return "NORMAL"
    except:
        return "ERROR"

def check_geo_danger(user_lat, user_lng):
    """Checks if user is inside a Hazard Zone"""
    if not user_lat or not user_lng:
        return None

    R = 6371000 # Earth radius in meters

    for zone in hazard_zones:
        # Calculate distance using simple trigonometry (Haversine approx)
        d_lat = math.radians(zone["lat"] - user_lat)
        d_lng = math.radians(zone["lng"] - user_lng)
        a = math.sin(d_lat/2)**2 + math.cos(math.radians(user_lat)) * math.cos(math.radians(zone["lat"])) * math.sin(d_lng/2)**2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
        distance = R * c

        if distance <= zone["radius"]:
            return zone['reason']
    return None

# 4. EVENT LISTENERS
@sio.event
async def connect(sid, environ):
    print(f"✅ User Connected: {sid}")

@sio.event
async def sensor_data(sid, data):
    # HANDLES CRASH DETECTION (Fast, runs 10x per second)
    status = check_crash(data)
    if status == "CRASH":
        print(f"⚠️ CRASH DETECTED for {sid}!")
        await sio.emit('force_sos_trigger', {'msg': 'Crash Detected!'}, room=sid)

@sio.event
async def location_update(sid, data):
    # HANDLES GPS CHECKS (Runs every few seconds)
    # The frontend must emit this event!
    lat = float(data.get('lat', 0))
    lng = float(data.get('lng', 0))
    
    danger_reason = check_geo_danger(lat, lng)
    
    if danger_reason:
        print(f"⚠️ HAZARD ZONE ENTERED: {danger_reason}")
        await sio.emit('force_warning', {'msg': f"Warning: {danger_reason}"}, room=sid)

@sio.event
async def disconnect(sid):
    print(f"❌ User Disconnected: {sid}")

# 5. RUN SERVER
if __name__ == "__main__":
    # Use 0.0.0.0 to allow mobile connections automatically
    uvicorn.run(socket_app, host="192.168.38.1", port=5000)