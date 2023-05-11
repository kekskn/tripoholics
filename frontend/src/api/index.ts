import axios from "axios";

export const getCurrentUser = async () => {
  const res = await fetch("http://localhost:8000/api/current_user/");
  return await res.json();
};

export const getUserDialogs = async () => {
  const res = await fetch(
    // `http://localhost:8000/api/dialogs/?user_id=${userId}`
    `http://localhost:8000/api/dialogs`
  );
  return await res.json();
};

export const getDialogMessages = async (dialogId) => {
  const res = await fetch(
    `http://localhost:8000/api/messages/?dialogId=${dialogId}`
  );
  return await res.json();
};

export const getUserPopupInfo = async (userId) => {
  const res = await fetch(
    `http://localhost:8000/api/user_popup_info/?user_id=${userId}`
  );
  return await res.json();
};

export const getDialogById = async (dialogId) => {
  const res = await fetch(
    `http://localhost:8000/api/dialogs/?dialog_id=${dialogId}`
  );
  return await res.json();
};

export const postCreateNewDialog = async (body) => {
  return await axios
    .post(`http://127.0.0.1:8000/api/dialogs/`, body)
    .then((res) => res.data)
    .catch((err) => ({ err }));
};

export const getEmptyDialogById = async (dialogId) => {
  const res = await fetch(
    `http://localhost:8000/api/dialogs/?emptyDialog_id=${dialogId}`
  );
  return await res.json();
};

export const sendMessage = async (body) => {
  return await axios
    .post(`http://127.0.0.1:8000/api/messages/`, body)
    .then((res) => res.data);
};
