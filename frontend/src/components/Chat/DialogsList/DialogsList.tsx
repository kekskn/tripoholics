import React, { useState } from "react";
import { useSelector } from "react-redux";
import { RootState } from "../../../redux/store";
import DialogItem from "../DialogItem/DialogItem";
import DialogsSearch from "../DialogsSearch/DialogsSearch";
import "./DialogsList.scss";
import renderSkeleton from "./helpers/renderSkeleton";

export default function DialogsList() {
  const user = useSelector((store: RootState) => store?.user);
  const dialogs = useSelector((store: RootState) => store?.chat?.dialogs);
  const [value, setValue] = useState("");

  const filteredDialogs = dialogs.filter((dialog) =>
    dialog.interlocutor.toLowerCase().includes(value.toLowerCase())
  );

  return (
    <div className="chat__dialogs-list">
      <DialogsSearch setValue={setValue} />
      <div className="chat__dialogs-list-wrapper">
        {dialogs.length
          ? filteredDialogs.map((dialog) => {
              return (
                <DialogItem
                  key={dialog.dialog_id}
                  date={new Date(Date.now() - 500000)}
                  companion={dialog.interlocutor}
                  roomName={dialog.dialog_id}
                  dialogId={dialog.dialog_id}
                  isEmptyDialog={dialog.isEmptyDialog}
                />
              );
            })
          : renderSkeleton()}
      </div>
    </div>
  );
}
