import React from "react";
import DialogItem from "../DialogItem/DialogItem";
import DialogsSearch from "../DialogsSearch/DialogsSearch";
import "./DialogsList.scss";

export default function DialogsList({ roomName }) {
  return (
    <div className="chat__dialogs-list">
      <DialogsSearch />
      <div className="chat__dialogs-list-wrapper">
        <DialogItem date={new Date(Date.now() - 500000)} roomName="q" />
        <DialogItem date={new Date(Date.now() - 9000000)} roomName="w" />
        <DialogItem date={new Date(Date.now() - 10000)} roomName="e" />
        <DialogItem date={new Date(Date.now() - 10000)} roomName="r" />
        <DialogItem date={new Date(Date.now() - 10000)} roomName="t" />
        <DialogItem date={new Date(Date.now() - 10000)} roomName="y" />
        <DialogItem date={new Date(Date.now() - 9000000)} roomName="u" />
        {/* <DialogItem date={new Date(Date.now() - 10000)} />
        <DialogItem date={new Date(Date.now() - 10000)} />
        <DialogItem date={new Date(Date.now() - 10000)} />
        <DialogItem date={new Date(Date.now() - 10000)} /> */}
      </div>
    </div>
  );
}
