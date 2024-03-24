from fastapi import FastAPI, Request
from typing import Dict
import json

app = FastAPI()

class Message(BaseModel):
    name: str
    message: str

@app.post("/predict")
async def predict(request: Request):
    data = await request.json()
    message = data["message"]
    # Here you can add the logic to process the message and generate a response
    response = {"answer": generate_response(message)}
    return response(content=json.dumps(response), media_type="application/json")

def generate_response(message: str):
    # Add the logic to generate a response based on the input message
    return "This is a generated response to the message: " + message

@app.get("/chat-history")
async def get_chat_history():
    # Here you can add the logic to retrieve the chat history from a database or another storage
    messages = [
        {"name": "User", "message": "Hello, Xen"},
        {"name": "Xen", "message": "Hi, how can I help you?"},
        {"name": "User", "message": "Can you tell me a joke?"},
        {"name": "Xen", "message": "Sure! Here's a joke: Why don't scientists trust atoms? Because they make up everything!"}
    ]
    return messages

@app.post("/send-message")
async def send_message(message: Message):
    # Here you can add the logic to send the message to the chatbot and update the chat history
    # For example, you can add the message to the list of messages and save it to a database
    messages = get_chat_history()
    messages.append(message)
    return {"message": "Message sent successfully"}

@app.get("/chatbox")
async def display_chatbox():
    return """
    <div class="chatbox">
        <div class="chatbox__button" onclick="toggleState(chatBox)">Open Chatbox</div>
        <div class="chatbox__support" style="display: none;">
            <div class="chatbox__messages"></div>
            <div class="chatbox__input">
                <input type="text" name="message" placeholder="Type a message here...">
                <button class="send__button" onclick="onSendButton(chatBox)">Send</button>
            </div>
        </div>
    </div>
    <script>
        let chatbox = document.querySelector('.chatbox__support');
        let messages = [];
        function toggleState(chatbox) {
            chatbox.style.display = (chatbox.style.display === 'block') ? 'none' : 'block';
        }
        function onSendButton(chatbox) {
            let message = chatbox.querySelector('input[name="message"]').value;
            if (message !== "") {
                sendMessage(message);
            }
        }
        function sendMessage(message) {
            fetch('/send-message', {
                method: 'POST',
                body: JSON.stringify({ name: 'User', message: message }),
                headers: {
                  'Content-Type': 'application/json'
                }
            })
            .then(r => r.json())
            .then(r => {
                messages.push({ name: "User", message: message });
                messages.push({ name: r.answer.name, message: r.answer.message });
                updateChatText(chatbox, messages);
            });
        }
        function updateChatText(chatbox, messages) {
            let chatmessage = chatbox.querySelector('.chatbox__messages');
            chatmessage.innerHTML = "";
            messages.slice().reverse().forEach(function(item) {
                if (item.name === "Xen")