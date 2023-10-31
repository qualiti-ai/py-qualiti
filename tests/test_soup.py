from bs4 import BeautifulSoup

HTML = """
<html><head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <title>OrangeHRM</title>
      <link rel="icon" href="/web/dist/favicon.ico?v=1689053487449">
    <link href="/web/dist/css/chunk-vendors.css?v=1689053487449" rel="preload" as="style">
    <link href="/web/dist/css/app.css?v=1689053487449" rel="preload" as="style">
    <link href="/web/dist/js/chunk-vendors.js?v=1689053487449" rel="preload" as="script">
    <link href="/web/dist/js/app.js?v=1689053487449" rel="preload" as="script">
      <link href="/web/dist/css/chunk-vendors.css?v=1689053487449" rel="stylesheet">
    <link href="/web/dist/css/app.css?v=1689053487449" rel="stylesheet">
<style type="text/css">
@font-face {
  font-weight: 400;
  font-style:  normal;
  font-family: circular;

  src: url('chrome-extension://liecbddmkiiihnedobmlmillhodjkdmb/fonts/CircularXXWeb-Book.woff2') format('woff2');
}

@font-face {
  font-weight: 700;
  font-style:  normal;
  font-family: circular;

  src: url('chrome-extension://liecbddmkiiihnedobmlmillhodjkdmb/fonts/CircularXXWeb-Bold.woff2') format('woff2');
}</style></head>
<body data-new-gr-c-s-check-loaded="14.1129.0" data-gr-ext-installed="">
  <style>
    :root {
            --oxd-primary-one-color:#FF7B1D;
            --oxd-primary-font-color:#FFFFFF;
            --oxd-secondary-four-color:#76BC21;
            --oxd-secondary-font-color:#FFFFFF;
            --oxd-primary-gradient-start-color:#FF920B;
            --oxd-primary-gradient-end-color:#F35C17;
            --oxd-secondary-gradient-start-color:#FF920B;
            --oxd-secondary-gradient-end-color:#F35C17;
            --oxd-primary-one-lighten-5-color:#ff8a37;
            --oxd-primary-one-lighten-30-color:#ffd4b6;
            --oxd-primary-one-darken-5-color:#ff6c03;
            --oxd-primary-one-alpha-10-color:rgba(255, 123, 29, 0.1);
            --oxd-primary-one-alpha-15-color:rgba(255, 123, 29, 0.15);
            --oxd-primary-one-alpha-20-color:rgba(255, 123, 29, 0.2);
            --oxd-primary-one-alpha-50-color:rgba(255, 123, 29, 0.5);
            --oxd-secondary-four-lighten-5-color:#84d225;
            --oxd-secondary-four-darken-5-color:#68a61d;
            --oxd-secondary-four-alpha-10-color:rgba(118, 188, 33, 0.1);
            --oxd-secondary-four-alpha-15-color:rgba(118, 188, 33, 0.15);
            --oxd-secondary-four-alpha-20-color:rgba(118, 188, 33, 0.2);
            --oxd-secondary-four-alpha-50-color:rgba(118, 188, 33, 0.5);
        }
  </style>
    <noscript>
        <strong>
            We're sorry but orangehrm doesn't work properly without JavaScript enabled. Please enable it to continue.
        </strong>
    </noscript>

    <div id="app" data-v-app=""><div class="orangehrm-login-layout" data-v-50815349="" data-v-358db50f=""><div class="orangehrm-login-layout-blob" data-v-50815349=""><div class="orangehrm-login-container" data-v-50815349=""><div class="orangehrm-login-slot-wrapper" data-v-50815349=""><div class="orangehrm-login-branding" data-v-3dda64e6="" data-v-50815349=""><img src="/web/images/ohrm_branding.png?v=1689053487449" alt="company-branding" data-v-3dda64e6=""></div><div class="orangehrm-login-slot" data-v-50815349=""><div class="orangehrm-login-logo-mobile" data-v-50815349=""><img src="/web/images/ohrm_logo.png" alt="orangehrm-logo" data-v-50815349=""></div><h5 class="oxd-text oxd-text--h5 orangehrm-login-title" data-v-7b563373="" data-v-358db50f="">Login</h5><div class="orangehrm-login-form" data-v-358db50f=""><div class="orangehrm-login-error" data-v-358db50f=""><!----><div class="oxd-sheet oxd-sheet--rounded oxd-sheet--gutters oxd-sheet--gray-lighten-2 orangehrm-demo-credentials" data-v-8a31f039="" data-v-358db50f=""><p class="oxd-text oxd-text--p" data-v-7b563373="" data-v-358db50f="">Username : Admin</p><p class="oxd-text oxd-text--p" data-v-7b563373="" data-v-358db50f="">Password : admin123</p></div></div><form class="oxd-form" novalidate="" method="post" action="/web/index.php/auth/validate" data-v-d5bfe35b="" data-v-358db50f=""><!----><input name="_token" type="hidden" value="5.oNmcGkgOx5tygA_ccOkfVMPp1OFUFtFLWz5xEkvpxhY.75_QLwl7hvEhtWG0Krp5AvG4oNYXe7MOamwfYDyOg3vHu_ZocUit1QbJfA" data-v-358db50f=""><div class="oxd-form-row" data-v-2130bd2a="" data-v-358db50f=""><div class="oxd-input-group oxd-input-field-bottom-space" data-v-957b4417="" data-v-358db50f=""><div class="oxd-input-group__label-wrapper" data-v-957b4417=""><i class="oxd-icon bi-person oxd-input-group__label-icon" data-v-bddebfba="" data-v-957b4417=""></i><label class="oxd-label" data-v-30ff22b1="" data-v-957b4417="">Username</label></div><div class="" data-v-957b4417=""><input class="oxd-input oxd-input--active" name="username" placeholder="Username" autofocus="" data-v-1f99f73c=""></div><!----></div></div><div class="oxd-form-row" data-v-2130bd2a="" data-v-358db50f=""><div class="oxd-input-group oxd-input-field-bottom-space" data-v-957b4417="" data-v-358db50f=""><div class="oxd-input-group__label-wrapper" data-v-957b4417=""><i class="oxd-icon bi-key oxd-input-group__label-icon" data-v-bddebfba="" data-v-957b4417=""></i><label class="oxd-label" data-v-30ff22b1="" data-v-957b4417="">Password</label></div><div class="" data-v-957b4417=""><input class="oxd-input oxd-input--active" type="password" name="password" placeholder="Password" data-v-1f99f73c=""></div><!----></div></div><div class="oxd-form-actions orangehrm-login-action" data-v-19c2496b="" data-v-358db50f=""><button type="submit" class="oxd-button oxd-button--medium oxd-button--main orangehrm-login-button" data-v-10d463b7="" data-v-358db50f=""><!----> Login <!----></button></div><div class="orangehrm-login-forgot" data-v-358db50f=""><p class="oxd-text oxd-text--p orangehrm-login-forgot-header" data-v-7b563373="" data-v-358db50f="">Forgot your password? </p></div></form><br data-v-358db50f=""></div><div class="orangehrm-login-footer" data-v-358db50f=""><div class="orangehrm-login-footer-sm" data-v-358db50f=""><a href="https://www.linkedin.com/company/orangehrm/mycompany/" target="_blank" data-v-358db50f=""><svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 500 500" role="presentation" class="oxd-icon orangehrm-sm-icon" data-v-bddebfba="" data-v-358db50f=""><g fill="currentColor"><path class="st0" d="M 250 0 C 387.99 0 500 112.01 500 250 C 500 387.99 387.99 500 250 500 C 112.01 500 0 387.99 0 250 C 0 112.01 112.01 0 250 0 Z M 171.814 390.523 L 171.814 195.261 L 106.945 195.261 L 106.945 390.523 L 171.814 390.523 Z M 405.883 390.523 L 405.883 278.595 C 405.883 218.627 373.857 190.768 331.128 190.768 C 296.732 190.768 281.291 209.722 272.631 223.039 L 272.631 195.261 L 207.762 195.261 C 208.66 213.562 207.762 390.523 207.762 390.523 L 272.631 390.523 L 272.631 281.454 C 272.631 275.653 273.04 269.771 274.755 265.604 C 279.412 253.921 290.115 241.912 308.089 241.912 C 331.536 241.912 340.932 259.804 340.932 286.029 L 340.932 390.523 L 405.883 390.523 Z M 139.788 101.144 C 117.566 101.144 103.105 115.768 103.105 134.885 C 103.105 153.595 117.157 168.627 138.971 168.627 L 139.379 168.627 C 162.01 168.627 176.062 153.595 176.062 134.885 C 175.654 115.686 162.01 101.144 139.788 101.144 Z" data-v-bddebfba=""></path></g></svg></a><a href="https://www.facebook.com/OrangeHRM/" target="_blank" data-v-358db50f=""><svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 500 500" role="presentation" class="oxd-icon orangehrm-sm-icon" data-v-bddebfba="" data-v-358db50f=""><g fill="currentColor"><path class="st0" d="M 249.02 500 L 249.266 500 L 249.182 500 L 249.02 500 Z M 250.818 500 L 250.98 500 L 250.818 500 Z M 248.284 500 L 248.529 500 L 248.364 500 L 248.284 500 Z M 251.634 500 L 251.469 500 L 251.714 500 L 251.634 500 Z M 247.55 500 L 247.712 500 L 247.55 500 Z M 252.451 500 L 252.287 500 L 252.451 500 Z M 253.267 500 L 253.432 500 L 253.267 500 Z M 246.57 500 L 246.812 500 L 246.732 500 L 246.57 500 Z M 254.003 500 L 253.839 500 L 254.085 500 L 254.003 500 Z M 245.832 500 L 246.077 500 L 245.915 500 L 245.832 500 Z M 254.819 499.917 L 254.657 499.917 L 254.819 499.917 Z M 245.098 499.917 L 245.343 499.917 L 245.098 499.917 Z M 244.199 499.917 L 244.445 499.917 L 244.199 499.917 Z M 255.637 499.917 L 255.799 499.917 L 255.637 499.917 Z M 243.382 499.917 L 243.71 499.917 L 243.627 499.917 L 243.382 499.917 Z M 256.455 499.917 L 256.372 499.917 L 256.7 499.917 L 256.455 499.917 Z M 257.273 499.917 L 257.108 499.917 L 257.435 499.917 L 257.273 499.917 Z M 242.647 499.917 L 242.974 499.917 L 242.809 499.917 L 242.647 499.917 Z M 241.913 499.836 L 242.158 499.836 L 241.913 499.836 L 241.747 499.836 L 241.913 499.836 Z M 258.088 499.836 L 257.842 499.836 L 258.088 499.836 L 258.253 499.836 L 258.088 499.836 Z M 258.822 499.836 L 258.742 499.836 L 259.071 499.836 L 258.822 499.836 Z M 240.933 499.836 L 241.26 499.836 L 241.178 499.836 L 240.933 499.836 Z M 240.197 499.836 L 240.522 499.836 L 240.36 499.836 L 240.197 499.836 Z M 259.64 499.836 L 259.478 499.836 L 259.805 499.836 L 259.64 499.836 Z M 239.46 499.755 L 239.788 499.755 L 239.46 499.755 Z M 260.458 499.755 L 260.212 499.755 L 260.458 499.755 Z M 238.479 499.755 L 238.888 499.755 L 238.808 499.755 L 238.479 499.755 Z M 261.274 499.755 L 261.192 499.755 L 261.6 499.755 L 261.274 499.755 Z M 237.745 499.671 L 238.152 499.671 L 237.99 499.671 L 237.745 499.671 Z M 262.092 499.671 L 261.927 499.671 L 262.337 499.671 L 262.092 499.671 Z M 237.01 499.671 L 237.417 499.671 L 237.172 499.671 L 237.01 499.671 Z M 262.828 499.671 L 262.583 499.671 L 262.99 499.671 L 262.828 499.671 Z M 263.644 499.671 L 263.317 499.671 L 263.644 499.671 L 263.97 499.671 L 263.644 499.671 Z M 236.354 499.671 L 236.683 499.671 L 236.354 499.671 L 235.947 499.671 L 236.354 499.671 Z M 264.459 499.593 L 264.297 499.593 L 264.708 499.593 L 264.459 499.593 Z M 235.294 499.593 L 235.703 499.593 L 235.539 499.593 L 235.294 499.593 Z M 234.64 499.509 L 235.05 499.509 L 234.802 499.509 L 234.64 499.509 Z M 265.277 499.509 L 265.032 499.509 L 265.441 499.509 L 265.277 499.509 Z M 233.905 499.509 L 234.232 499.509 L 233.905 499.509 L 233.577 499.509 L 233.905 499.509 Z M 266.013 499.509 L 265.687 499.509 L 266.013 499.509 L 266.34 499.509 L 266.013 499.509 Z M 266.829 499.428 L 266.748 499.428 L 267.158 499.428 L 266.829 499.428 Z M 232.925 499.428 L 233.333 499.428 L 233.252 499.428 L 232.925 499.428 Z M 232.189 499.347 L 232.597 499.347 L 232.435 499.347 L 232.189 499.347 Z M 267.647 499.347 L 267.485 499.347 L 267.893 499.347 L 267.647 499.347 Z M 231.455 499.347 L 231.782 499.347 L 231.455 499.347 Z M 268.462 499.347 L 268.22 499.347 L 268.462 499.347 Z M 230.555 499.264 L 230.882 499.264 L 230.8 499.264 L 230.555 499.264 Z M 269.2 499.264 L 269.445 499.264 L 269.2 499.264 Z M 270.014 499.182 L 269.852 499.182 L 270.179 499.182 L 270.014 499.182 Z M 229.819 499.182 L 230.148 499.182 L 229.984 499.182 L 229.819 499.182 Z M 229.085 499.099 L 229.33 499.099 L 229.085 499.099 Z M 270.832 499.182 L 270.67 499.182 L 270.832 499.182 Z M 228.35 499.099 Z M 271.57 499.099 Z M 272.385 499.02 L 272.468 499.02 L 272.385 499.02 Z M 227.532 499.02 L 227.697 499.02 L 227.615 499.02 L 227.532 499.02 Z M 226.798 498.937 L 226.96 498.937 L 226.798 498.937 Z M 273.202 498.937 L 273.122 498.937 L 273.202 498.937 Z M 210.947 496.977 C 91.503 478.185 0 374.672 0 250 C 0 112.009 112.009 0 250 0 C 387.989 0 500 112.009 500 250 C 500 374.672 408.497 478.185 289.052 496.977 L 289.052 322.302 L 347.305 322.302 L 358.415 250 L 289.052 250 L 289.052 203.104 C 289.052 183.332 298.775 164.053 329.82 164.053 L 361.355 164.053 L 361.355 102.533 C 361.355 102.533 332.762 97.63 305.392 97.63 C 248.284 97.63 210.947 132.27 210.947 194.935 L 210.947 250 L 147.467 250 L 147.467 322.302 L 210.947 322.302 L 210.947 496.977 Z" data-v-bddebfba=""></path></g></svg></a><a href="https://twitter.com/orangehrm?lang=en" target="_blank" data-v-358db50f=""><svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 500 500" role="presentation" class="oxd-icon orangehrm-sm-icon" data-v-bddebfba="" data-v-358db50f=""><g fill="currentColor"><path class="st0" d="M 250 0 C 387.99 0 500 112.01 500 250 C 500 387.99 387.99 500 250 500 C 112.01 500 0 387.99 0 250 C 0 112.01 112.01 0 250 0 Z M 205.964 383.006 C 316.585 383.006 377.042 291.34 377.042 211.928 C 377.042 209.314 377.042 206.699 376.879 204.167 C 388.562 195.67 398.856 185.049 406.944 172.957 C 396.242 177.696 384.64 180.964 372.386 182.435 C 384.886 174.918 394.363 163.235 398.856 149.101 C 387.255 155.964 374.428 160.948 360.703 163.725 C 349.755 152.042 334.15 144.771 316.83 144.771 C 283.66 144.771 256.699 171.732 256.699 204.902 C 256.699 209.64 257.189 214.216 258.333 218.627 C 208.333 216.095 164.052 192.157 134.395 155.801 C 129.248 164.624 126.307 175 126.307 185.948 C 126.307 206.781 136.928 225.245 153.105 235.948 C 143.219 235.703 133.987 232.925 125.899 228.431 L 125.899 229.167 C 125.899 258.333 146.569 282.516 174.183 288.154 C 169.199 289.542 163.807 290.278 158.333 290.278 C 154.493 290.278 150.735 289.869 146.977 289.134 C 154.575 313.072 176.797 330.392 203.105 330.882 C 182.516 346.977 156.618 356.536 128.431 356.536 C 123.529 356.536 118.791 356.291 114.052 355.637 C 140.359 372.957 172.059 383.006 205.964 383.006 Z" data-v-bddebfba=""></path></g></svg></a><a href="https://www.youtube.com/c/OrangeHRMInc" target="_blank" data-v-358db50f=""><svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 500 500" role="presentation" class="oxd-icon orangehrm-sm-icon" data-v-bddebfba="" data-v-358db50f=""><g fill="currentColor"><path class="st0" d="M 250 0 C 387.99 0 499.999 112.01 499.999 250 C 499.999 387.99 387.99 500 250 500 C 112.009 500 0 387.99 0 250 C 0 112.01 112.009 0 250 0 Z M 399.754 174.755 C 396.16 161.275 385.539 150.735 372.14 147.141 C 347.794 140.605 250.081 140.605 250.081 140.605 C 250.081 140.605 152.369 140.605 128.022 147.141 C 114.542 150.735 104.003 161.356 100.408 174.755 C 93.872 199.101 93.872 250 93.872 250 C 93.872 250 93.872 300.817 100.408 325.245 C 104.003 338.725 114.624 349.265 128.022 352.859 C 152.369 359.395 250.081 359.395 250.081 359.395 C 250.081 359.395 347.794 359.395 372.14 352.859 C 385.62 349.265 396.16 338.644 399.754 325.245 C 406.29 300.899 406.29 250 406.29 250 C 406.29 250 406.29 199.183 399.754 174.755 Z M 218.709 296.895 L 218.709 203.105 L 299.918 250 L 218.709 296.895 Z" data-v-bddebfba=""></path></g></svg></a></div><div class="orangehrm-copyright-wrapper"><p class="oxd-text oxd-text--p orangehrm-copyright" data-v-7b563373="">OrangeHRM OS 5.5</p><p class="oxd-text oxd-text--p orangehrm-copyright" data-v-7b563373="">© 2005 - 2023 <a href="http://www.orangehrm.com" target="_blank">OrangeHRM, Inc</a>. All rights reserved.</p></div></div></div></div></div><div class="orangehrm-login-logo" data-v-50815349=""><img src="/web/images/ohrm_logo.png" alt="orangehrm-logo" data-v-50815349=""></div></div></div><div class="oxd-toast-container oxd-toast-container--bottom" id="oxd-toaster_1"></div></div>
    <script type="text/javascript">
        window.appGlobal = {
          baseUrl: "/web/index.php",
          publicPath: "/web",
        };
    </script>
    <script src="/web/dist/js/chunk-vendors.js?v=1689053487449"></script>
    <script src="/web/dist/js/app.js?v=1689053487449"></script>


<div id="loom-companion-mv3" ext-id="liecbddmkiiihnedobmlmillhodjkdmb"><section id="shadow-host-companion"></section></div></body><grammarly-desktop-integration data-grammarly-shadow-root="true"></grammarly-desktop-integration></html>
"""


def test_soup():
    soup = BeautifulSoup(HTML, "html.parser")
    # Descendants: 132
    url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    title = soup.find("title").text
    soup.find("head").extract()
    [tag.extract() for tag in soup.find_all("script")]
    [tag.extract() for tag in soup.find_all("noscript")]
    [tag.extract() for tag in soup.find_all("style")]
    [tag.extract() for tag in soup.find_all("g")]
    [tag.extract() for tag in soup.find_all("path")]

    # Descendants: 86
    print("\n", soup.encode().decode().strip())

    """
    * What should we do if the HTML is too large?
    """
