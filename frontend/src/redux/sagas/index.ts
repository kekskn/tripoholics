import { all } from "axios";
import {
  take,
  takeLeading,
  takeEvery,
  takeLatest,
  put,
  call,
  fork,
  select,
} from "redux-saga/effects";
import {
  getCurrentUser,
  getDialogById,
  getDialogMessages,
  getEmptyDialogById,
  getUserDialogs,
  postCreateNewDialog,
  sendMessage,
} from "../../api";

import {
  addNewMessage,
  // fetchMessages,
  sendNewMessage,
  setUserInfo,
  setCurrentDialog,
  setDialogs,
  setMessages,
  getCurrentDialog,
  getCurrentEmptyDialog,
  fetchDialog,
  onLoad,
  createNewDialog,
  fetchNewDialog,
  openNewDialog,
} from "../actions";
import { GET_CURRENT_DIALOG, ON_LOAD } from "../constants";

export function* handleUserInfo() {
  try {
    /**
     * получаем инфу о текущем авторизованном юзере и сохраняем ее в стор
     */
    const userInfo = yield call(getCurrentUser);
    yield put(setUserInfo(userInfo));

    yield call(handleUserDialogs, userInfo.id);
    console.log("after handleUserInfo");
    // yield call(fetchDialogInfoById);
  } catch (error) {
    throw new Error(`Error while getting current user info: ${error}`);
  }
}

export function* handleUserDialogs(userId: number) {
  try {
    /**
     * получаем диалоги текущего юзера и сохраняем их в стор
     */
    const userDialogs = yield call(getUserDialogs);
    yield put(setDialogs(userDialogs));
  } catch (error) {
    throw new Error(`Error while getting current user dialogs: ${error}`);
  }
}

export function* fetchDialogMessages(action) {
  try {
    const messages = yield getDialogMessages(action.payload);
    yield put(setMessages(messages));
  } catch {
    throw new Error("Error while getting current user");
  }
}

export function* onSendNewMessage(action) {
  try {
    const { success } = yield sendMessage(action.payload);
  } catch {
    throw new Error("Error while getting current user");
  }
}

export function* handleCurrentDialog({ payload }) {
  try {
    const currentUser = yield select((state) => state.user);
    if (!currentUser.id) yield call(handleUserInfo);
    yield put(fetchDialog());
    const user = yield select(({ user }) => user);
    const { first_user_fio, second_user_fio, first_user_id, second_user_id } =
      yield call(getDialogById, payload);

    let companion, companion_id;
    if (first_user_fio === `${user.name} ${user.surname}`) {
      companion = second_user_fio;
    } else {
      companion = first_user_fio;
    }

    if (user.id === first_user_id) companion_id = second_user_id;
    else companion_id = first_user_id;

    yield put(setCurrentDialog({ companion, companion_id, dialogId: payload }));
    const messages = yield call(getDialogMessages, payload);

    yield put(setMessages(messages));
  } catch {
    throw new Error("Error while getting current dialog");
  }
}

export function* handleCurrentEmptyDialog({ payload }) {
  try {
    const currentUser = yield select((state) => state.user);
    if (!currentUser.id) yield call(handleUserInfo);
    yield put(fetchDialog());
    const { interlocutor, interlocutor_id } = yield call(
      getEmptyDialogById,
      payload
    );

    yield put(
      setCurrentDialog({
        companion: interlocutor,
        companion_id: interlocutor_id,
        dialogId: payload,
      })
    );
    yield put(setMessages([]));
  } catch {
    throw new Error("Error while getting current dialog");
  }
}

export function* handleCreateNewDialog(action) {
  try {
    yield put(fetchNewDialog());
    const { success, dialogId, err } = yield call(
      postCreateNewDialog,
      action.payload
    );
    console.log("res new dialog: ", success, err);

    yield put(openNewDialog());

    if (success) {
      console.log("res success");
      window.open(`http://localhost:8000/my_messages/new_dialog/${dialogId}`);
    } else if (err.response.data.error === "Real dialog already exists") {
      window.open(
        `http://localhost:8000/my_messages/${err.response.data.dialogId}`
      );
    } else if (err.response.data.error === "Empty dialog already exists") {
      window.open(
        `http://localhost:8000/my_messages/new_dialog/${err.response.data.dialogId}`
      );
    }
  } catch (err) {
    throw new Error(`Error while creating new dialog: ${err}`);
  }
}

export default function* rootSaga() {
  yield takeLatest(ON_LOAD, handleUserInfo);
  // yield takeLatest(fetchDialog, fetchDialogMessages);
  yield takeLatest(sendNewMessage, onSendNewMessage);
  yield takeLatest(getCurrentDialog, handleCurrentDialog);
  yield takeLatest(getCurrentEmptyDialog, handleCurrentEmptyDialog);
  yield takeLatest(createNewDialog, handleCreateNewDialog);
}
