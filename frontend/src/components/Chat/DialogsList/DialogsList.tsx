import React from "react";
import DialogItem from "../DialogItem/DialogItem";
import DialogsSearch from "../DialogsSearch/DialogsSearch";
import "./DialogsList.scss";

export default function DialogsList() {
  return (
    <div className="chat__dialogs-list">
      <DialogsSearch />
      <div className="chat__dialogs-list-wrapper">
        <DialogItem date={new Date(Date.now() - 500000)} />
        <DialogItem date={new Date(Date.now() - 9000000)} />
        <DialogItem date={new Date(Date.now() - 10000)} />
        <DialogItem date={new Date(Date.now() - 10000)} />
        <DialogItem date={new Date(Date.now() - 10000)} />
        <DialogItem date={new Date(Date.now() - 10000)} />
        <DialogItem date={new Date(Date.now() - 10000)} />
        <DialogItem date={new Date(Date.now() - 500000)} />
        <DialogItem date={new Date(Date.now() - 9000000)} />
        <DialogItem date={new Date(Date.now() - 10000)} />
        <DialogItem date={new Date(Date.now() - 10000)} />
        <DialogItem date={new Date(Date.now() - 10000)} />
        <DialogItem date={new Date(Date.now() - 10000)} />
        <DialogItem date={new Date(Date.now() - 10000)} />
      </div>
    </div>
  );
}
