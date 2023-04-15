import React, { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { changeDialogInterlocutorStatus } from "src/redux/actions";
import { RootState } from "../../../redux/store";
import DialogItem from "../DialogItem/DialogItem";
import DialogsSearch from "../DialogsSearch/DialogsSearch";
import "./DialogsList.scss";
import renderSkeleton from "./helpers/renderSkeleton";

export default function DialogsList() {
  const dispatch = useDispatch();
  const user = useSelector((store: RootState) => store?.user);
  const dialogs = useSelector((store: RootState) => store?.chat?.dialogs);
  const [value, setValue] = useState("");

  const filteredDialogs = dialogs.filter((dialog) =>
    dialog.interlocutor.toLowerCase().includes(value.toLowerCase())
  );

  useEffect(() => {
    for (let d of dialogs) {
      const socket = new WebSocket(
        `ws://localhost:8000/ws/online_status/${d.interlocutor_id}/`
      );

      socket.onmessage = function (event) {
        const data = JSON.parse(event.data);
        console.log("WebSocket message received:", data);
        if (
          dialogs.find((d) => d.interlocutor_id === data.user_id).is_online !==
          data.is_online
        )
          dispatch(changeDialogInterlocutorStatus(data));
      };
      socket.onclose = function (event) {
        console.log("WebSocket disconnected");
      };
    }
  }, [dialogs]);

  return (
    <div className="chat__dialogs-list">
      <DialogsSearch setValue={setValue} />
      <div className="chat__dialogs-list-wrapper">
        {dialogs.length
          ? filteredDialogs.map((d) => {
              return (
                <DialogItem
                  key={d.dialog_id}
                  companion={d.interlocutor}
                  dialogId={d.dialog_id}
                  isEmptyDialog={d.isEmptyDialog}
                  isOnline={d.is_online}
                  lastMessage={d.last_message}
                />
              );
            })
          : renderSkeleton()}
      </div>
    </div>
  );
}
