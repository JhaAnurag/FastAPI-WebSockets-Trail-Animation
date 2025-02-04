
# FastAPI-WebSockets-Trail-Animation

A simple real-time multiplayer demo showcasing trail animation using FastAPI, WebSockets, and JavaScript.  This project allows multiple users to connect through a WebSocket and see each other's cursor trails rendered dynamically in their browsers.  Parameters like trail behavior and colors are customizable and synchronized across all connected clients in real-time.

## Features

- **Real-time Multiplayer Interaction:** See the trails of other users in the same browser session, updated live.
- **Smooth Trail Animation:** Utilizes second-order dynamics for smooth and responsive cursor following.
- **Customizable Parameters:**
    - **Frequency (f):** Controls the speed of the follower's response.
    - **Damping (z):**  Affects the oscillation and smoothness of the follower.
    - **Response (r):** Adjusts the overall responsiveness to cursor movements.
    - **Trail Length (s):**  Determines how long the trail behind each cursor persists.
    - **Trail Color:** Choose a color for the trail.
    - **Circle Color:** Select the color of the cursor circle.
    - **Rainbow Trail:** Option to enable a rainbow effect for the trail.
- **Simple and Clean UI:**  User-friendly interface with controls easily accessible.
- **Uses FastAPI and WebSockets:**  Built with modern, high-performance technologies for backend and real-time communication.

## Technologies Used

- **Backend:**
    - [FastAPI](https://fastapi.tiangolo.com/): A modern, fast (high-performance), web framework for building APIs with Python 3.7+ based on standard Python type hints.
    - [WebSockets](https://developer.mozilla.org/en-US/docs/Web/API/WebSocket_API): For real-time, bidirectional communication between the server and clients.
    - [uvicorn](https://www.uvicorn.org/): An ASGI web server for running FastAPI applications.
    - [orjson](https://github.com/ijl/orjson):  Fast, correct Python JSON library.
    - [asyncio](https://docs.python.org/3/library/asyncio.html):  Python's built-in asynchronous I/O framework.

- **Frontend:**
    - HTML5, CSS3, JavaScript: For structuring, styling, and implementing the interactive animation in the browser.

## Setup and Run

**Prerequisites:**

- Python 3.7 or higher

**Installation:**

1. Clone this repository:
   ```bash
   git clone https://github.com/JhaAnurag/FastAPI-WebSockets-Trail-Animation.git
   cd FastAPI-WebSockets-Trail-Animation
   ```

2. Create a virtual environment (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Linux/macOS
   venv\Scripts\activate  # On Windows
   ```

3. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```
   *(Create a `requirements.txt` file in the project root with the following content if it doesn't exist)*:
   ```
   fastapi
   uvicorn
   orjson
   ```

**Running the Server:**

1. Navigate to the project directory in your terminal.

2. Run the FastAPI application using uvicorn:
   ```bash
   uvicorn server:app --reload
   ```
   This command starts the server on `http://127.0.0.1:8000` (or `http://0.0.0.0:8000` if you want to access it from other devices on the network). The `--reload` flag enables automatic server restarts upon code changes, useful for development.

**Accessing the Frontend:**

1. Open your web browser and go to `http://localhost:8000`.
2. Open multiple browser windows or tabs to the same address to see the multiplayer interaction.

## Usage

1. **Open in Multiple Browsers:**  To experience the multiplayer aspect, open the `http://localhost:8000` URL in multiple browser windows or on different devices connected to the same network.
2. **Move Your Mouse/Touch:**  Move your mouse cursor or touch the screen within the browser window. You will see a colored circle and a trail following your cursor.
3. **Observe Other Users:** You will see the colored circles and trails of other users who are connected to the same server instance in real-time.
4. **Customize Controls:**
   - Click the "⚙️" button in the top-left corner to open the controls panel.
   - **Name Input:** Enter a name to identify yourself to other users.
   - **Frequency (f), Damping (z), Response (r):** Adjust these sliders or number inputs to modify the behavior of your cursor follower. Higher frequency makes it faster, damping affects oscillation, and response scales the overall responsiveness.
   - **Trail Length (s):**  Control the duration of your trail. Higher values result in longer trails.
   - **Trail Color:** Click the color input to choose a color for your trail.
   - **Circle Color:** Click the color input to select the color of your cursor circle.
   - **Rainbow Trail:** Check the box to enable a rainbow effect for your trail.
5. **Real-time Updates:**  Any changes you make in the controls panel (name, parameters, colors) are instantly synchronized with all other connected clients.

## License

[MIT License](LICENSE) (You can add a LICENSE file if you wish to use the MIT License or another license).

---

Enjoy experimenting with real-time trail animations!
