"use strict";

function confirmDelete(event) {
  if (!confirm("確定刪除這筆留言？")) {
    event.preventDefault();
  }
}
