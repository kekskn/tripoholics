import React from "react";
import DialogItem from "../DialogItem/DialogItem";
import "./DialogsList.scss";

export default function DialogsList() {
  return (
    <div className="chat__dialogs-list">
      <DialogItem />
      <DialogItem />
      <DialogItem />
    </div>
  );
}
