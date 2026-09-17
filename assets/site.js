document.documentElement.classList.add('js');
const toggle = document.querySelector('.nav-toggle');
const nav = document.querySelector('#site-nav');
function closeMenu() { nav?.classList.remove('open'); toggle?.setAttribute('aria-expanded', 'false'); }
if (toggle && nav) {
  toggle.hidden = false;
  toggle.addEventListener('click', () => {
    const open = nav.classList.toggle('open');
    toggle.setAttribute('aria-expanded', String(open));
  });
  nav.addEventListener('click', event => { if (event.target.closest('a')) closeMenu(); });
  document.addEventListener('keydown', event => {
    if (event.key === 'Escape' && nav.classList.contains('open')) { closeMenu(); toggle.focus(); }
  });
  document.addEventListener('click', event => { if (!event.target.closest('.site-header')) closeMenu(); });
  matchMedia('(min-width: 1101px)').addEventListener('change', closeMenu);
}
const filters = document.querySelector('#record-filters');
if (filters) {
  filters.hidden = false;
  const search = document.querySelector('#record-search');
  const kind = document.querySelector('#record-kind');
  const items = [...document.querySelectorAll('[data-record]')];
  const count = document.querySelector('#record-count');
  const empty = document.querySelector('#record-empty');
  const apply = () => {
    const query = search.value.trim().toLocaleLowerCase();
    let visible = 0;
    for (const item of items) {
      const match = (!kind.value || item.dataset.kind === kind.value) && (!query || item.textContent.toLocaleLowerCase().includes(query));
      item.hidden = !match;
      if (match) visible++;
    }
    count.textContent = `${visible} / ${items.length}`;
    empty.hidden = visible !== 0;
  };
  search.addEventListener('input', apply);
  kind.addEventListener('change', apply);
  apply();
}

// Keep the mailto fallback, but offer an in-page draft when dialogs are supported.
const inquiry = document.querySelector('#inquiry-dialog');
if (inquiry && typeof inquiry.showModal === 'function') {
  const english = document.documentElement.lang === 'en';
  const t = (zh, en) => english ? en : zh;
  const email = inquiry.querySelector('#inquiry-email');
  const subject = inquiry.querySelector('#inquiry-subject');
  const body = inquiry.querySelector('#inquiry-body');
  const status = inquiry.querySelector('#inquiry-status');
  const manual = inquiry.querySelector('#inquiry-manual');
  const copyText = inquiry.querySelector('#inquiry-copy-text');
  const mail = inquiry.querySelector('#inquiry-mail');
  const gmail = inquiry.querySelector('#inquiry-gmail');
  const drafts = new Map();
  let trigger;
  let activeKey;

  function updateDraft() {
    const query = new URLSearchParams({subject: subject.value, body: body.value});
    mail.href = `mailto:${email.value}?${query.toString().replace(/\+/g, '%20')}`;
    const compose = new URL('https://mail.google.com/mail/');
    compose.search = new URLSearchParams({view: 'cm', fs: '1', to: email.value, su: subject.value, body: body.value}).toString();
    gmail.href = compose.href;
    drafts.set(activeKey, {subject: subject.value, body: body.value});
  }

  for (const link of document.querySelectorAll('[data-inquiry]')) {
    link.setAttribute('aria-haspopup', 'dialog');
    link.setAttribute('aria-controls', 'inquiry-dialog');
    link.addEventListener('click', event => {
      if (event.button !== 0 || event.metaKey || event.ctrlKey || event.shiftKey || event.altKey) return;
      event.preventDefault();
      trigger = link;
      activeKey = link.href;
      const url = new URL(link.href);
      const title = url.searchParams.get('subject') || t('合作洽詢', 'Work with Wilbur');
      const draft = drafts.get(activeKey) || {subject: title, body: url.searchParams.get('body') || ''};
      email.value = decodeURIComponent(url.pathname);
      subject.value = draft.subject;
      body.value = draft.body;
      inquiry.querySelector('#inquiry-title').textContent = title;
      status.textContent = '';
      manual.hidden = true;
      updateDraft();
      inquiry.showModal();
      document.documentElement.classList.add('inquiry-open');
      inquiry.scrollTop = 0;
    });
  }

  for (const field of [subject, body]) {
    field.addEventListener('input', () => {
      updateDraft();
      status.textContent = '';
      manual.hidden = true;
    });
  }
  inquiry.querySelector('.inquiry-close').addEventListener('click', () => inquiry.close());
  inquiry.addEventListener('close', () => {
    if (inquiry.open) return;
    document.documentElement.classList.remove('inquiry-open');
    trigger?.focus({preventScroll: true});
  });
  inquiry.addEventListener('click', event => {
    const rect = inquiry.getBoundingClientRect();
    if (event.target === inquiry && (event.clientX < rect.left || event.clientX > rect.right || event.clientY < rect.top || event.clientY > rect.bottom)) inquiry.close();
  });

  async function copy(text, success) {
    try {
      if (!navigator.clipboard?.writeText) throw new Error('Clipboard unavailable');
      await navigator.clipboard.writeText(text);
      manual.hidden = true;
      status.textContent = success;
    } catch {
      copyText.value = text;
      manual.hidden = false;
      copyText.focus();
      copyText.select();
      status.textContent = t('無法自動複製，已選取文字。請使用裝置的複製功能。', 'Automatic copying is unavailable. The text is selected; use your device’s Copy command.');
    }
  }
  inquiry.querySelector('#inquiry-copy-email').addEventListener('click', () => copy(email.value, t('已複製信箱。', 'Email address copied.')));
  inquiry.querySelector('#inquiry-copy').addEventListener('click', () => {
    const message = `${t('收件人', 'To')}: ${email.value}\n${t('主旨', 'Subject')}: ${subject.value}\n\n${body.value}`;
    copy(message, t('已複製收件人、主旨與內容，可貼到你的信箱使用。', 'Recipient, subject and message copied. Paste them into your email.'));
  });
  mail.addEventListener('click', () => {
    status.textContent = t('若郵件程式沒有開啟，可使用 Gmail 或「複製整封信件」。', 'If no email app opens, use Gmail or Copy full message.');
  });
  gmail.addEventListener('click', () => {
    status.textContent = t('將在新分頁開啟 Gmail。若未帶入內容，可先複製整封信件再貼上。', 'Gmail opens in a new tab. If the draft is not filled in, copy and paste the full message.');
  });
}
