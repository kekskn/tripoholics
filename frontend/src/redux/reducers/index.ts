import { combineReducers } from "redux";
import chatSlice from "./chat";
import userSlice from "./user";

const reducer = combineReducers({
  user: userSlice.reducer,
  chat: chatSlice.reducer,
});

export default reducer;
