set -e

# Start athe API

# If an old uvicorn is running, kill it so we don’t leak processes
pkill -f "uvicorn api:app" 2>/dev/null || true

echo "Starting FastAPI backend…"
pushd backend > /dev/null

# Start uvicorn in the background (logs to backend/uvicorn.log)
nohup uvicorn api:app --reload --host 127.0.0.1 --port 8000 \
  > uvicorn.log 2>&1 &

echo "API started (pid $!) and logging to backend/uvicorn.log"
popd > /dev/null

# Fire up the simulator
DEVICE="iPhone 16 Pro"

echo "Booting Simulator \"$DEVICE\"…"
# Boot the device (won’t error if already booted)
xcrun simctl boot "$DEVICE" 2>/dev/null || true
# Show the Simulator UI so you can see your app
open -a Simulator

# Give it a sec
sleep 2

# Launch the swift iOS app in the Simulator

echo "Building and launching iOS app in Simulator…"
pushd mobile/TrainingPlan > /dev/null

# Build the project
xcodebuild \
  -project TrainingPlan.xcodeproj \
  -scheme TrainingPlan \
  -configuration Debug \
  -sdk iphonesimulator \
  -derivedDataPath build \
  build \
  > build.log 2>&1

echo "Build complete (see mobile/TrainingPlan/build.log)"

# Install & run on the booted simulator
APP_PATH="build/Build/Products/Debug-iphonesimulator/TrainingPlan.app"
xcrun simctl install booted "$APP_PATH"
xcrun simctl launch booted MAP.TrainingPlan

popd > /dev/null

echo "App Running"