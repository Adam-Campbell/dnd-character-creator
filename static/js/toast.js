const toastEl = document.getElementById('toast');
const toastMessageEl = document.getElementById('toast-message-container');
let toastInstance;

const noop = () => { };
let currentCallback = noop;

const variantClasses = {
    'danger': 'alert alert-danger',
    'success': 'alert alert-success',
};

const defaultOptions = {
    delay: 5000,
    variant: 'danger',
    callback: noop,
};


if (toastEl) {
    // Add event listener to the toast element (which is always in
    // the DOM). When the toast is hidden, clear the message and
    // call the current callback, then dispose of the toast instance.
    toastEl.addEventListener('hidden.bs.toast', () => {
        toastMessageEl.innerText = '';
        // currentCallback is stored in a closure, so we can call it here
        // and it will always be the callback that was set when the most
        // recent toast was shown.
        currentCallback();
        currentCallback = noop;
        toastInstance.dispose();
    });
}


/**
 * @typedef {Object} ToastOptions
 * @property {number} delay
 * @property {string} variant
 * @property {Function} callback
 */

/**
 * Display a toast with the given message and options. If options are not provided,
 * defaults to a danger variant, 5000ms delay, and a no-op callback.
 * @param {string} message 
 * @param {ToastOptions} options
 * @returns {void}
 */
export function showToast(message, options={}) {
    const { delay, variant, callback } = { ...defaultOptions, ...options };
    toastInstance = new bootstrap.Toast(toastEl, { delay });
    currentCallback = callback;
    toastMessageEl.innerText = message;
    toastMessageEl.className = variantClasses[variant];
    toastInstance.show();
}

