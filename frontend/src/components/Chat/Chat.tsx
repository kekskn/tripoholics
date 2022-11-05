import React from "react";
import "./Chat.scss";
import { headerHeightCalc } from "../../utils/headerHeightCalc";
import DialogsList from "./DialogsList/DialogsList";
import MessagesBlock from "./MessagesBlock/MessagesBlock";

export default function Chat() {
  return (
    <div className="chat">
      <DialogsList />
      <MessagesBlock />
    </div>
  );
}
