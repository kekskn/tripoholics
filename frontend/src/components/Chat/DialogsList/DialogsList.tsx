import React from "react";
import DialogItem from "../DialogItem/DialogItem";
import "./DialogsList.scss";

export default function DialogsList() {
  return (
    <div className="chat__dialogs-list">
      <DialogItem date={new Date(Date.now() - 500000)} />
      <DialogItem date={new Date(Date.now() - 9000000)} />
      <DialogItem date={new Date(Date.now() - 10000)} />
      <DialogItem date={new Date(Date.now() - 10000)} />
      <DialogItem date={new Date(Date.now() - 10000)} />
      <DialogItem date={new Date(Date.now() - 10000)} />
      <DialogItem date={new Date(Date.now() - 10000)} />
    </div>
  );
}
