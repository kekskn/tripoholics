import { useParams } from "react-router-dom";
import React from "react";
import "./Chat.scss";
import DialogsList from "./DialogsList/DialogsList";
import MessagesBlock from "./MessagesBlock/MessagesBlock";
import EmptyChat from "./MessagesBlock/EmptyChat/EmptyChat";

export default function Chat() {
  const { roomName } = useParams();
  console.log("roomName: ", roomName);
  return (
    <div className="chat">
      <DialogsList />
      {roomName ? <MessagesBlock /> : <EmptyChat />}
    </div>
  );
}
