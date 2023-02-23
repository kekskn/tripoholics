import { useParams } from "react-router-dom";
import React, { useEffect, useState } from "react";
import axios from "axios";
import "./Chat.scss";
import DialogsList from "./DialogsList/DialogsList";
import MessagesBlock from "./MessagesBlock/MessagesBlock";
import EmptyChat from "./MessagesBlock/EmptyChat/EmptyChat";

export default function Chat() {
  const { roomName } = useParams();
  const [messages, setMessages] = useState([]);
  console.log("roomName: ", roomName);

  async function getMessages() {
    // let response;
    await axios
      .get("http://127.0.0.1:8000/api/messages?dialogId=1")
      .then((data) => {
        console.log("data:", data);
        setMessages(data.data);
      });
    // return response;
  }
  useEffect(() => {
    getMessages();
    // console.log("response mes: ", response);
  }, []);
  console.log("messages: ", messages);
  return (
    <div className="chat">
      <DialogsList roomName={roomName} />
      {roomName ? <MessagesBlock /> : <EmptyChat />}
    </div>
  );
}
