export default function renderDialogItemMessage(message, isMy) {
  const newMessage = `${isMy ? "Вы: " : ""}${message}`;
  if (newMessage.length > 40) return `${newMessage.slice(0, 40)}...`;
  return newMessage;
}
