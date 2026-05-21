# Changelog

## 1.7.0 (2026-05-21)

Full Changelog: [v1.6.0...v1.7.0](https://github.com/Not-Diamond/not-diamond-python/compare/v1.6.0...v1.7.0)

### Features

* **api:** api update ([c174dfe](https://github.com/Not-Diamond/not-diamond-python/commit/c174dfed54777b32b3727f8a299f89f3318c0a68))
* **internal/types:** support eagerly validating pydantic iterators ([d6f52d9](https://github.com/Not-Diamond/not-diamond-python/commit/d6f52d91b321157b527650a5b525378837adfb08))
* support setting headers via env ([e4d8142](https://github.com/Not-Diamond/not-diamond-python/commit/e4d8142f6fe05accf9529e2aea146d73732c764c))


### Bug Fixes

* **client:** add missing f-string prefix in file type error message ([b976e15](https://github.com/Not-Diamond/not-diamond-python/commit/b976e150b7dbb398824d3385a86b197432bfd5c2))
* use correct field name format for multipart file arrays ([75a23a9](https://github.com/Not-Diamond/not-diamond-python/commit/75a23a9d44a396770a2a68e421ac68f9777e0dd9))


### Performance Improvements

* **client:** optimize file structure copying in multipart requests ([2d57d0c](https://github.com/Not-Diamond/not-diamond-python/commit/2d57d0c0e41e16d137dfb34a1b86452f1b7582dd))


### Chores

* **internal:** more robust bootstrap script ([31301e1](https://github.com/Not-Diamond/not-diamond-python/commit/31301e18564d5d487dab1a1f565d9b6a393ee76d))
* **internal:** reformat pyproject.toml ([b0436af](https://github.com/Not-Diamond/not-diamond-python/commit/b0436af903a26176f31d65f2595e59601b999f1f))
* **tests:** bump steady to v0.22.1 ([6ecea7e](https://github.com/Not-Diamond/not-diamond-python/commit/6ecea7e18281ab3bc1f2b28f4cfcac3a427d4e1e))


### Documentation

* improve examples ([7c71ae5](https://github.com/Not-Diamond/not-diamond-python/commit/7c71ae5933c951c669a512fd8e0c7952a148b015))
* update examples ([8e37eca](https://github.com/Not-Diamond/not-diamond-python/commit/8e37eca91e4d36e7a8260503ea0ffa9b4c43e662))

## 1.6.0 (2026-04-11)

Full Changelog: [v1.5.1...v1.6.0](https://github.com/Not-Diamond/not-diamond-python/compare/v1.5.1...v1.6.0)

### Features

* **api:** api update ([aeadd13](https://github.com/Not-Diamond/not-diamond-python/commit/aeadd131bb55464a890d7d7efa52582dce89806f))
* **internal:** implement indices array format for query and form serialization ([2dfa6b8](https://github.com/Not-Diamond/not-diamond-python/commit/2dfa6b863c29ad5165ca63ca34baeca3ece2d9c3))


### Bug Fixes

* **client:** preserve hardcoded query params when merging with user params ([79afa6a](https://github.com/Not-Diamond/not-diamond-python/commit/79afa6a54502a5cbdd379ff56354d2b698a981b0))
* **deps:** bump minimum typing-extensions version ([b534367](https://github.com/Not-Diamond/not-diamond-python/commit/b53436721bbcb8e1dad0b87cb9ee33db389323aa))
* ensure file data are only sent as 1 parameter ([21155cb](https://github.com/Not-Diamond/not-diamond-python/commit/21155cba0c37c064b7f0494e94423687c1c9d1e6))
* **pydantic:** do not pass `by_alias` unless set ([491e554](https://github.com/Not-Diamond/not-diamond-python/commit/491e554ed5dded8b7a2420af0f9ac031928f416d))
* sanitize endpoint path params ([4ae88e9](https://github.com/Not-Diamond/not-diamond-python/commit/4ae88e926ed96c26f1241ba27d40f21992218077))


### Chores

* **ci:** skip lint on metadata-only changes ([3248e26](https://github.com/Not-Diamond/not-diamond-python/commit/3248e2698ce1b356ac929d5695194eab00ed36eb))
* **ci:** skip uploading artifacts on stainless-internal branches ([b476f66](https://github.com/Not-Diamond/not-diamond-python/commit/b476f661bf4048cb8deaaad5f4f10a39c6676c44))
* **internal:** add request options to SSE classes ([0318c8c](https://github.com/Not-Diamond/not-diamond-python/commit/0318c8cbe29b70892c2838ce0399c4712058e077))
* **internal:** make `test_proxy_environment_variables` more resilient ([bf042c7](https://github.com/Not-Diamond/not-diamond-python/commit/bf042c78c266ad77f3e037f9971dfdec55e691f3))
* **internal:** make `test_proxy_environment_variables` more resilient to env ([02c3a32](https://github.com/Not-Diamond/not-diamond-python/commit/02c3a32aa289e14786a0a766a75724eced87f822))
* **internal:** tweak CI branches ([74c1977](https://github.com/Not-Diamond/not-diamond-python/commit/74c19775794f33b2d12bd71e6381590f956363f7))
* **internal:** update gitignore ([9830e49](https://github.com/Not-Diamond/not-diamond-python/commit/9830e492bce485b52911658ce2444326332e2e7b))
* **test:** do not count install time for mock server timeout ([81d9b5b](https://github.com/Not-Diamond/not-diamond-python/commit/81d9b5b41f20e1decbd150a4c2b5aaa717fa5dad))
* **tests:** bump steady to v0.19.4 ([d0163e4](https://github.com/Not-Diamond/not-diamond-python/commit/d0163e4ec9450816c45512d386e458fba938e5f6))
* **tests:** bump steady to v0.19.5 ([56d8074](https://github.com/Not-Diamond/not-diamond-python/commit/56d807440c7a8d2e0cd4d57d4f1db991e2c78380))
* **tests:** bump steady to v0.19.6 ([a0ea487](https://github.com/Not-Diamond/not-diamond-python/commit/a0ea4879ed19b394ba449420aae345295c032135))
* **tests:** bump steady to v0.19.7 ([93a6177](https://github.com/Not-Diamond/not-diamond-python/commit/93a6177d3eea65c15f84994c1ae6556b17842b04))
* **tests:** bump steady to v0.20.1 ([7b7196a](https://github.com/Not-Diamond/not-diamond-python/commit/7b7196ad0e52c0aba5fb268c23992d40d4bd75ae))
* **tests:** bump steady to v0.20.2 ([6dd4973](https://github.com/Not-Diamond/not-diamond-python/commit/6dd4973a2d4cb944bfb893307d3beda74c1e2603))
* update mock server docs ([ce8f436](https://github.com/Not-Diamond/not-diamond-python/commit/ce8f436984c0e46ed4d53c276add66e0603e3de0))
* update placeholder string ([7767361](https://github.com/Not-Diamond/not-diamond-python/commit/7767361d016bc23b67bc7c968adba90453108896))


### Refactors

* **tests:** switch from prism to steady ([7693765](https://github.com/Not-Diamond/not-diamond-python/commit/769376567e6fbcd46ce1d378d763c7d348b3cfe1))

## 1.5.1 (2026-02-13)

Full Changelog: [v1.5.0...v1.5.1](https://github.com/Not-Diamond/not-diamond-python/compare/v1.5.0...v1.5.1)

### Chores

* format all `api.md` files ([8febad2](https://github.com/Not-Diamond/not-diamond-python/commit/8febad237de882dd951430312e9405550d886a80))
* **internal:** bump dependencies ([fd1873d](https://github.com/Not-Diamond/not-diamond-python/commit/fd1873d2be995bff5a50365213c684a4373c6a25))
* **internal:** fix lint error on Python 3.14 ([c8f2481](https://github.com/Not-Diamond/not-diamond-python/commit/c8f2481d092ee82c6912a1965a79de732ce29ef3))

## 1.5.0 (2026-01-30)

Full Changelog: [v1.4.0...v1.5.0](https://github.com/Not-Diamond/not-diamond-python/compare/v1.4.0...v1.5.0)

### Features

* **client:** add custom JSON encoder for extended type support ([4e78c03](https://github.com/Not-Diamond/not-diamond-python/commit/4e78c03979aef5612cd26cc655ad8ac8dae5f4c2))

## 1.4.0 (2026-01-24)

Full Changelog: [v1.3.0...v1.4.0](https://github.com/Not-Diamond/not-diamond-python/compare/v1.3.0...v1.4.0)

### Features

* add Slack notification workflow for new pull requests ([97535a3](https://github.com/Not-Diamond/not-diamond-python/commit/97535a3158340c4dce76370718068ebd412e64e9))
* **api:** api update ([365a9ae](https://github.com/Not-Diamond/not-diamond-python/commit/365a9ae2999395edcb4578b150a184f90039a4d3))
* **api:** api update ([db00ca9](https://github.com/Not-Diamond/not-diamond-python/commit/db00ca90b883b9b184139ad5fecafd54d33b184d))
* **api:** api update ([a4e0f68](https://github.com/Not-Diamond/not-diamond-python/commit/a4e0f68210e1ef3cb167dde09cf331c63e48a5d4))
* **api:** api update ([40c19d5](https://github.com/Not-Diamond/not-diamond-python/commit/40c19d56ea8e303b0aa455e6a67b136fb9b489d4))
* **api:** api update ([979a984](https://github.com/Not-Diamond/not-diamond-python/commit/979a984a047066066a690babec82c61552f3ab24))
* **api:** api update ([3a75371](https://github.com/Not-Diamond/not-diamond-python/commit/3a753710842884d465ded98567ba3408adf05848))
* **api:** api update ([80741ad](https://github.com/Not-Diamond/not-diamond-python/commit/80741adc8c0dddc791ffc9b680385baf8beba1a0))
* **api:** api update ([e6cc0b3](https://github.com/Not-Diamond/not-diamond-python/commit/e6cc0b3f0f5fd5a4d8ac2a0b66070a67b0986ec9))
* **api:** api update ([9514729](https://github.com/Not-Diamond/not-diamond-python/commit/9514729f30190892396343daddbc8c6d657edbc8))
* **api:** api update ([12c16a2](https://github.com/Not-Diamond/not-diamond-python/commit/12c16a218d211c47aaad82ad672f668a27715edf))
* **api:** api update ([bdb1ebe](https://github.com/Not-Diamond/not-diamond-python/commit/bdb1ebe855fe24f1c9d93804fea1ef38ae77341d))
* **api:** api update ([0cdedc2](https://github.com/Not-Diamond/not-diamond-python/commit/0cdedc27ef1bab63e433bdc0717c36cc48d60b55))
* **api:** api update ([f717b91](https://github.com/Not-Diamond/not-diamond-python/commit/f717b91a37cd48a63e9ef9458cef6dd899383f2c))
* **api:** api update ([24340ab](https://github.com/Not-Diamond/not-diamond-python/commit/24340ab121937a85e9c4bbc8b644c62b15f75d89))
* **api:** api update ([f4f83bd](https://github.com/Not-Diamond/not-diamond-python/commit/f4f83bd926d4296f883f5db75de90a5db275867a))
* **api:** api update ([d403264](https://github.com/Not-Diamond/not-diamond-python/commit/d4032647605736f1c51d04023d3adb24f448737f))
* **api:** api update ([c7a1198](https://github.com/Not-Diamond/not-diamond-python/commit/c7a1198c1432e833b740f92df9996379f941228f))
* **api:** api update ([9265a0a](https://github.com/Not-Diamond/not-diamond-python/commit/9265a0a3959818b06f157726e68d3c73f7f5d9c9))
* **api:** api update ([880c195](https://github.com/Not-Diamond/not-diamond-python/commit/880c195dc41ac5e500cae9b9a71b0840f97e7556))
* **api:** changed name ([a5fbbc6](https://github.com/Not-Diamond/not-diamond-python/commit/a5fbbc6174cd362389bd1e3848f2b870bdf37837))
* **api:** enable tests ([64ccd03](https://github.com/Not-Diamond/not-diamond-python/commit/64ccd03281ae7b420b44cf64910568e3657f24db))
* **api:** exclude non sdk endpoints ([fb04bc4](https://github.com/Not-Diamond/not-diamond-python/commit/fb04bc460d7f9f7f191cffcb56868d09fa45edc1))
* **api:** fix missing endpoint ([427d1d3](https://github.com/Not-Diamond/not-diamond-python/commit/427d1d3bdd7be290e66897aa35daba984931e4a4))
* **api:** fix modelSelect error ([eb29990](https://github.com/Not-Diamond/not-diamond-python/commit/eb29990fab14468f39368f7f5b0e4ebf019d0841))
* **api:** manual updates ([4f5cbc8](https://github.com/Not-Diamond/not-diamond-python/commit/4f5cbc86230f35d5eaa7421e5c794fe037b32b92))
* **api:** manual updates ([88af4f8](https://github.com/Not-Diamond/not-diamond-python/commit/88af4f89785cdc1dc070cc8ba59bf209f05960eb))
* **api:** manual updates ([ac84aab](https://github.com/Not-Diamond/not-diamond-python/commit/ac84aab2c200e5681d4717355064ebdf32c19831))
* **api:** manual updates ([3de5719](https://github.com/Not-Diamond/not-diamond-python/commit/3de57198fad333e98cb6d32df8a1cb3cecf997dc))
* **api:** manual updates ([f10b3cf](https://github.com/Not-Diamond/not-diamond-python/commit/f10b3cf27f9ce359c020e1a2e1ac8cf66e1f8c35))
* **api:** manual updates ([48af7c1](https://github.com/Not-Diamond/not-diamond-python/commit/48af7c13347f7db5ef8e0063c8e5f8363d092d01))
* **api:** manual updates ([ae9b855](https://github.com/Not-Diamond/not-diamond-python/commit/ae9b855e1d9ec3dccdd96bd121ac11aba1402981))
* **api:** manual updates ([3b34f4f](https://github.com/Not-Diamond/not-diamond-python/commit/3b34f4fb9f5ed2281a5672179f759f7eccb41dc0))
* **api:** manual updates ([50911a0](https://github.com/Not-Diamond/not-diamond-python/commit/50911a023f29a7017ec810e55ee55209c5dbdacc))
* **api:** manual updates ([1d846ce](https://github.com/Not-Diamond/not-diamond-python/commit/1d846ce29e4e8688e82bd64d500d3752af77d6de))
* **api:** manual updates ([e864113](https://github.com/Not-Diamond/not-diamond-python/commit/e864113c227997b0c04a02cad05b8963fe5a9283))
* **api:** manual updates ([0a7ac49](https://github.com/Not-Diamond/not-diamond-python/commit/0a7ac4986879837b1b93bb31c5b7e6d211a55077))
* **api:** manual updates ([dd9657d](https://github.com/Not-Diamond/not-diamond-python/commit/dd9657df2226d7d46cf99ee8b23eced653155c74))
* **api:** manual updates ([b905d72](https://github.com/Not-Diamond/not-diamond-python/commit/b905d72ebec4d42373de62865a85f62d4a87c477))
* **api:** manual updates ([d664d8d](https://github.com/Not-Diamond/not-diamond-python/commit/d664d8d20ab802a9aa0150519a3900d386f7b1d9))
* **api:** manual updates ([603c1b7](https://github.com/Not-Diamond/not-diamond-python/commit/603c1b74c64850e1fd8a89e08b1d66d0665188e0))
* **api:** manual updates ([42fb39e](https://github.com/Not-Diamond/not-diamond-python/commit/42fb39e0978aa329f4b5171ff54aaab257558135))
* **api:** manual updates ([9ee8b3e](https://github.com/Not-Diamond/not-diamond-python/commit/9ee8b3e1220e45b00ce9c9078ab7f54bb1e34e19))
* **api:** manual updates ([8062369](https://github.com/Not-Diamond/not-diamond-python/commit/80623692c7da0db7c57b7953af3ec9fdc1e0fca2))
* **api:** regen docs ([c80dbe1](https://github.com/Not-Diamond/not-diamond-python/commit/c80dbe1994cd73b549995b5e91ac86a62a77f5b7))
* **api:** report group ([4312188](https://github.com/Not-Diamond/not-diamond-python/commit/43121880104978fa2b88a3ad0e85070a2b322787))
* **api:** update nomenclature ([413eff4](https://github.com/Not-Diamond/not-diamond-python/commit/413eff4789d2187c0502eccc106bf987ea2f55fe))
* **api:** verify mock tests enabled ([638d79b](https://github.com/Not-Diamond/not-diamond-python/commit/638d79bdd90097d9823d02e3dac8b12ab2849d03))
* **client:** add support for binary request streaming ([8b9ac11](https://github.com/Not-Diamond/not-diamond-python/commit/8b9ac113ad23c8b30fcb360ad46dad41f5ea970f))
* enhance Slack PR notification to include 'ready for review' status and additional details ([af8afd5](https://github.com/Not-Diamond/not-diamond-python/commit/af8afd5aa9253bac48f0600c06eb649c66a3b2d7))


### Bug Fixes

* **client:** close streams without requiring full consumption ([c9f7310](https://github.com/Not-Diamond/not-diamond-python/commit/c9f73103e1747f06da439c77b7d5e322c4d09a4e))
* compat with Python 3.14 ([566b7bf](https://github.com/Not-Diamond/not-diamond-python/commit/566b7bf3583a41330dc9ada230e343fc852dd7ad))
* **compat:** update signatures of `model_dump` and `model_dump_json` for Pydantic v1 ([1417077](https://github.com/Not-Diamond/not-diamond-python/commit/14170771cd8e66d2aab39bd5b866dfd081eb45f0))
* ensure streams are always closed ([94cd458](https://github.com/Not-Diamond/not-diamond-python/commit/94cd458b5027c72a25b0ea0f9dce70f0f11c738e))
* **types:** allow pyright to infer TypedDict types within SequenceNotStr ([5663881](https://github.com/Not-Diamond/not-diamond-python/commit/566388145d7d3fea2e52158963fc2ad8e8ee45c8))
* use async_to_httpx_files in patch method ([132c94c](https://github.com/Not-Diamond/not-diamond-python/commit/132c94c38fc007f6f687a5d66f50fd3955065eb4))


### Chores

* add missing docstrings ([003db35](https://github.com/Not-Diamond/not-diamond-python/commit/003db35899fda442fd45bdcafe4aeaad09b1dd4d))
* add Python 3.14 classifier and testing ([9acba74](https://github.com/Not-Diamond/not-diamond-python/commit/9acba7453c5da79029dc88dc074a844e8bf025b4))
* **api:** changed default client name to NotDiamond ([28f6709](https://github.com/Not-Diamond/not-diamond-python/commit/28f6709fe254d7ab07bbb74b7f516f25cfd9c3c6))
* bump `httpx-aiohttp` version to 0.1.9 ([37d5de2](https://github.com/Not-Diamond/not-diamond-python/commit/37d5de2162ece6024539d9e546dd2679ba5e1882))
* **ci:** upgrade `actions/github-script` ([352e6a8](https://github.com/Not-Diamond/not-diamond-python/commit/352e6a838f991fd91157f192f2761141dbf17311))
* **deps:** mypy 1.18.1 has a regression, pin to 1.17 ([578a964](https://github.com/Not-Diamond/not-diamond-python/commit/578a964fd65e2d01aaf61aeedcf1d9c471447aa1))
* **docs:** update README with new prompt adaptation examples and enable prototype mode ([bcaa9e8](https://github.com/Not-Diamond/not-diamond-python/commit/bcaa9e86cc0fe32c3a339d5bf85fed5d24246ef1))
* **docs:** use environment variables for authentication in code snippets ([4493c72](https://github.com/Not-Diamond/not-diamond-python/commit/4493c723b56c4f402327fca66a47f755b09a5bc3))
* **internal/tests:** avoid race condition with implicit client cleanup ([14e720b](https://github.com/Not-Diamond/not-diamond-python/commit/14e720b4d735b9a52d634b1ec24db5bff9c3aa24))
* **internal:** add `--fix` argument to lint script ([448c196](https://github.com/Not-Diamond/not-diamond-python/commit/448c1962fc32893b4cd7ace7d2a1c1b1a8beb479))
* **internal:** add missing files argument to base client ([47b12a0](https://github.com/Not-Diamond/not-diamond-python/commit/47b12a06b94576bd12bc4dcba24a5bb8ced59f8e))
* **internal:** codegen related update ([b26fdeb](https://github.com/Not-Diamond/not-diamond-python/commit/b26fdeb30acc5c5b4e26ae1d1dd76dbee69ca09b))
* **internal:** detect missing future annotations with ruff ([316a749](https://github.com/Not-Diamond/not-diamond-python/commit/316a7493d166e631eafcc888d377dbe340178b24))
* **internal:** grammar fix (it's -&gt; its) ([6d37a12](https://github.com/Not-Diamond/not-diamond-python/commit/6d37a125457223046183bcc8ee7159ed96b80424))
* **internal:** update `actions/checkout` version ([15211cd](https://github.com/Not-Diamond/not-diamond-python/commit/15211cd2310f289b894c358840e4c122fea68515))
* **package:** drop Python 3.8 support ([8f6e2eb](https://github.com/Not-Diamond/not-diamond-python/commit/8f6e2eb71d0523fa1d7b6bb39c30ffbbc95363cf))
* remove commented-out line for bot notification exclusion in Slack PR workflow ([e0c337e](https://github.com/Not-Diamond/not-diamond-python/commit/e0c337ed9a951826b060204809180d074ca79c88))
* remove condition to exclude bot users from Slack notification in PR workflow ([776b597](https://github.com/Not-Diamond/not-diamond-python/commit/776b597086b06869bca76818eaaaaca4e4940531))
* speedup initial import ([b3ceca0](https://github.com/Not-Diamond/not-diamond-python/commit/b3ceca0f4500850259e8a438ac95c8b2da343915))
* update lockfile ([8b040bc](https://github.com/Not-Diamond/not-diamond-python/commit/8b040bc315c0cf48380efb8578b7a197ef654413))
* update SDK settings ([227346c](https://github.com/Not-Diamond/not-diamond-python/commit/227346c8e801e2ee7f0f7c376fb55e5aea606232))
* update SDK settings ([ba3968b](https://github.com/Not-Diamond/not-diamond-python/commit/ba3968b9ef7b2ec9e7b1b3983a6e2a8b31ccbc37))
* update SDK settings ([26ae314](https://github.com/Not-Diamond/not-diamond-python/commit/26ae3141eaa1df28dd8b1d1e5d322fb135bee6b9))
* update SDK settings ([ecc0dc6](https://github.com/Not-Diamond/not-diamond-python/commit/ecc0dc63a8d98e9d2178f04cebde730257bae353))


### Documentation

* update README to include example of initializing NotDiamond client with API key ([3f3a1e5](https://github.com/Not-Diamond/not-diamond-python/commit/3f3a1e5ca3911eada1a2c0abfa1c2c5d0bf75cbc))
* update README to reflect changes in Prompt Adaptation details and streamline key features section ([71f97f8](https://github.com/Not-Diamond/not-diamond-python/commit/71f97f8348e2fb21af321ac7965d53e3fb88211f))
* update README to reflect changes in prompt adaptation method names and remove outdated async usage section ([c793b18](https://github.com/Not-Diamond/not-diamond-python/commit/c793b18630bf398ae32bcb2d5adfdf91cc65c8f9))
* update README to remove outdated Prompt Adaptation section and add new examples for intelligent model routing and training a custom router. ([17b08b6](https://github.com/Not-Diamond/not-diamond-python/commit/17b08b65ef604d68e766c0cb16cee70d0cd4d575))


### Refactors

* **README:** update terminology from "Prompt Adaptation" to "Prompt Optimization" and adjust related code examples ([7cb7d97](https://github.com/Not-Diamond/not-diamond-python/commit/7cb7d97793b6a5f20f0b122aedccbe328dfe2bc0))

## 1.3.0 (2026-01-17)

Full Changelog: [v1.2.2...v1.3.0](https://github.com/Not-Diamond/not-diamond-python/compare/v1.2.2...v1.3.0)

### Features

* **api:** manual updates ([4f5cbc8](https://github.com/Not-Diamond/not-diamond-python/commit/4f5cbc86230f35d5eaa7421e5c794fe037b32b92))


### Chores

* **internal:** update `actions/checkout` version ([15211cd](https://github.com/Not-Diamond/not-diamond-python/commit/15211cd2310f289b894c358840e4c122fea68515))

## 1.2.2 (2026-01-16)

Full Changelog: [v1.2.1...v1.2.2](https://github.com/Not-Diamond/not-diamond-python/compare/v1.2.1...v1.2.2)

## 1.2.1 (2026-01-15)

Full Changelog: [v1.2.0...v1.2.1](https://github.com/Not-Diamond/not-diamond-python/compare/v1.2.0...v1.2.1)

### Features

* **api:** manual updates ([7c53e94](https://github.com/Not-Diamond/not-diamond-python/commit/7c53e9422d28da27ad6bddc91273bd20dcc177db))

## 1.2.0 (2026-01-15)

Full Changelog: [v1.1.3...v1.2.0](https://github.com/Not-Diamond/not-diamond-python/compare/v1.1.3...v1.2.0)

### Features

* **api:** api update ([db00ca9](https://github.com/Not-Diamond/not-diamond-python/commit/db00ca90b883b9b184139ad5fecafd54d33b184d))
* **api:** manual updates ([ac84aab](https://github.com/Not-Diamond/not-diamond-python/commit/ac84aab2c200e5681d4717355064ebdf32c19831))
* **api:** update nomenclature ([413eff4](https://github.com/Not-Diamond/not-diamond-python/commit/413eff4789d2187c0502eccc106bf987ea2f55fe))
* **client:** add support for binary request streaming ([8b9ac11](https://github.com/Not-Diamond/not-diamond-python/commit/8b9ac113ad23c8b30fcb360ad46dad41f5ea970f))

## 1.1.3 (2026-01-12)

Full Changelog: [v1.1.2...v1.1.3](https://github.com/Not-Diamond/not-diamond-python/compare/v1.1.2...v1.1.3)

### Features

* add Slack notification workflow for new pull requests ([97535a3](https://github.com/Not-Diamond/not-diamond-python/commit/97535a3158340c4dce76370718068ebd412e64e9))
* **api:** api update ([616dcaa](https://github.com/Not-Diamond/not-diamond-python/commit/616dcaa965dc5fde8d79dfa2ce01ad14f1d5ab91))
* enhance Slack PR notification to include 'ready for review' status and additional details ([af8afd5](https://github.com/Not-Diamond/not-diamond-python/commit/af8afd5aa9253bac48f0600c06eb649c66a3b2d7))


### Chores

* remove commented-out line for bot notification exclusion in Slack PR workflow ([e0c337e](https://github.com/Not-Diamond/not-diamond-python/commit/e0c337ed9a951826b060204809180d074ca79c88))
* remove condition to exclude bot users from Slack notification in PR workflow ([776b597](https://github.com/Not-Diamond/not-diamond-python/commit/776b597086b06869bca76818eaaaaca4e4940531))

## 1.1.2 (2025-12-19)

Full Changelog: [v1.1.1...v1.1.2](https://github.com/Not-Diamond/not-diamond-python/compare/v1.1.1...v1.1.2)

### Chores

* **internal:** add `--fix` argument to lint script ([448c196](https://github.com/Not-Diamond/not-diamond-python/commit/448c1962fc32893b4cd7ace7d2a1c1b1a8beb479))

## 1.1.1 (2025-12-18)

Full Changelog: [v1.1.0...v1.1.1](https://github.com/Not-Diamond/not-diamond-python/compare/v1.1.0...v1.1.1)

### Bug Fixes

* use async_to_httpx_files in patch method ([edc6ef8](https://github.com/Not-Diamond/not-diamond-python/commit/edc6ef8ed4023637b73f77a60d671118490149ad))


### Chores

* speedup initial import ([6a70606](https://github.com/Not-Diamond/not-diamond-python/commit/6a706065bd55c616c38d10f3fa1c13cd6e32ca99))

## 1.1.0 (2025-12-16)

Full Changelog: [v1.0.1...v1.1.0](https://github.com/Not-Diamond/not-diamond-python/compare/v1.0.1...v1.1.0)

### Features

* **api:** api update ([aa449df](https://github.com/Not-Diamond/not-diamond-python/commit/aa449df78f1d0aa8d6714f375cd2075df4456837))
* **api:** api update ([b5cbefd](https://github.com/Not-Diamond/not-diamond-python/commit/b5cbefd0b1ce6ee883e7847510b9f5fd5ad22899))


### Chores

* **api:** changed default client name to NotDiamond ([8599dc8](https://github.com/Not-Diamond/not-diamond-python/commit/8599dc8db216ea164a04f781fd12b9455d00366c))
* **internal:** add missing files argument to base client ([6a2fc27](https://github.com/Not-Diamond/not-diamond-python/commit/6a2fc2744efef181cbf6a413e3e35bda38c79a1a))

## 1.0.1 (2025-12-09)

Full Changelog: [v1.0.0...v1.0.1](https://github.com/Not-Diamond/not-diamond-python/compare/v1.0.0...v1.0.1)

### Bug Fixes

* **types:** allow pyright to infer TypedDict types within SequenceNotStr ([5663881](https://github.com/Not-Diamond/not-diamond-python/commit/566388145d7d3fea2e52158963fc2ad8e8ee45c8))


### Chores

* add missing docstrings ([003db35](https://github.com/Not-Diamond/not-diamond-python/commit/003db35899fda442fd45bdcafe4aeaad09b1dd4d))

## 1.0.0 (2025-12-08)

Full Changelog: [v1.0.0-rc18...v1.0.0](https://github.com/Not-Diamond/not-diamond-python/compare/v1.0.0-rc18...v1.0.0)

### Features

* **api:** api update ([d35e3bf](https://github.com/Not-Diamond/not-diamond-python/commit/d35e3bf24a62a770d70ccc9627b5136d6ea4e4de))

## 1.0.0-rc18 (2025-12-08)

Full Changelog: [v1.0.0-rc17...v1.0.0-rc18](https://github.com/Not-Diamond/not-diamond-python/compare/v1.0.0-rc17...v1.0.0-rc18)

### Chores

* **docs:** update README with new prompt adaptation examples and enable prototype mode ([bcaa9e8](https://github.com/Not-Diamond/not-diamond-python/commit/bcaa9e86cc0fe32c3a339d5bf85fed5d24246ef1))

## 1.0.0-rc17 (2025-12-08)

Full Changelog: [v1.0.0-rc16...v1.0.0-rc17](https://github.com/Not-Diamond/not-diamond-python/compare/v1.0.0-rc16...v1.0.0-rc17)

### Features

* **api:** api update ([80741ad](https://github.com/Not-Diamond/not-diamond-python/commit/80741adc8c0dddc791ffc9b680385baf8beba1a0))
* **api:** api update ([e6cc0b3](https://github.com/Not-Diamond/not-diamond-python/commit/e6cc0b3f0f5fd5a4d8ac2a0b66070a67b0986ec9))
* **api:** api update ([9514729](https://github.com/Not-Diamond/not-diamond-python/commit/9514729f30190892396343daddbc8c6d657edbc8))
* **api:** manual updates ([3de5719](https://github.com/Not-Diamond/not-diamond-python/commit/3de57198fad333e98cb6d32df8a1cb3cecf997dc))


### Bug Fixes

* ensure streams are always closed ([94cd458](https://github.com/Not-Diamond/not-diamond-python/commit/94cd458b5027c72a25b0ea0f9dce70f0f11c738e))


### Chores

* add Python 3.14 classifier and testing ([9acba74](https://github.com/Not-Diamond/not-diamond-python/commit/9acba7453c5da79029dc88dc074a844e8bf025b4))
* **deps:** mypy 1.18.1 has a regression, pin to 1.17 ([578a964](https://github.com/Not-Diamond/not-diamond-python/commit/578a964fd65e2d01aaf61aeedcf1d9c471447aa1))
* **docs:** use environment variables for authentication in code snippets ([4493c72](https://github.com/Not-Diamond/not-diamond-python/commit/4493c723b56c4f402327fca66a47f755b09a5bc3))
* update lockfile ([8b040bc](https://github.com/Not-Diamond/not-diamond-python/commit/8b040bc315c0cf48380efb8578b7a197ef654413))

## 1.0.0-rc16 (2025-11-14)

Full Changelog: [v1.0.0-rc15...v1.0.0-rc16](https://github.com/Not-Diamond/not-diamond-python/compare/v1.0.0-rc15...v1.0.0-rc16)

### Features

* **api:** manual updates ([f10b3cf](https://github.com/Not-Diamond/not-diamond-python/commit/f10b3cf27f9ce359c020e1a2e1ac8cf66e1f8c35))


### Documentation

* update README to reflect changes in prompt adaptation method names and remove outdated async usage section ([c793b18](https://github.com/Not-Diamond/not-diamond-python/commit/c793b18630bf398ae32bcb2d5adfdf91cc65c8f9))

## 1.0.0-rc15 (2025-11-14)

Full Changelog: [v1.0.0-rc14...v1.0.0-rc15](https://github.com/Not-Diamond/not-diamond-python/compare/v1.0.0-rc14...v1.0.0-rc15)

### Features

* **api:** api update ([12c16a2](https://github.com/Not-Diamond/not-diamond-python/commit/12c16a218d211c47aaad82ad672f668a27715edf))

## 1.0.0-rc14 (2025-11-14)

Full Changelog: [v1.0.0-rc13...v1.0.0-rc14](https://github.com/Not-Diamond/not-diamond-python/compare/v1.0.0-rc13...v1.0.0-rc14)

### Features

* **api:** manual updates ([48af7c1](https://github.com/Not-Diamond/not-diamond-python/commit/48af7c13347f7db5ef8e0063c8e5f8363d092d01))

## 1.0.0-rc13 (2025-11-13)

Full Changelog: [v1.0.0-rc12...v1.0.0-rc13](https://github.com/Not-Diamond/not-diamond-python/compare/v1.0.0-rc12...v1.0.0-rc13)

### Features

* **api:** manual updates ([ae9b855](https://github.com/Not-Diamond/not-diamond-python/commit/ae9b855e1d9ec3dccdd96bd121ac11aba1402981))


### Documentation

* update README to include example of initializing NotDiamond client with API key ([3f3a1e5](https://github.com/Not-Diamond/not-diamond-python/commit/3f3a1e5ca3911eada1a2c0abfa1c2c5d0bf75cbc))
* update README to reflect changes in Prompt Adaptation details and streamline key features section ([71f97f8](https://github.com/Not-Diamond/not-diamond-python/commit/71f97f8348e2fb21af321ac7965d53e3fb88211f))
* update README to remove outdated Prompt Adaptation section and add new examples for intelligent model routing and training a custom router. ([17b08b6](https://github.com/Not-Diamond/not-diamond-python/commit/17b08b65ef604d68e766c0cb16cee70d0cd4d575))

## 1.0.0-rc12 (2025-11-12)

Full Changelog: [v1.0.0-rc11...v1.0.0-rc12](https://github.com/Not-Diamond/not-diamond-python/compare/v1.0.0-rc11...v1.0.0-rc12)

### Bug Fixes

* **compat:** update signatures of `model_dump` and `model_dump_json` for Pydantic v1 ([1417077](https://github.com/Not-Diamond/not-diamond-python/commit/14170771cd8e66d2aab39bd5b866dfd081eb45f0))


### Chores

* **internal:** codegen related update ([b26fdeb](https://github.com/Not-Diamond/not-diamond-python/commit/b26fdeb30acc5c5b4e26ae1d1dd76dbee69ca09b))

## 1.0.0-rc11 (2025-11-11)

Full Changelog: [v1.0.0-rc10...v1.0.0-rc11](https://github.com/Not-Diamond/not-diamond-python/compare/v1.0.0-rc10...v1.0.0-rc11)

### Features

* **api:** changed name ([a5fbbc6](https://github.com/Not-Diamond/not-diamond-python/commit/a5fbbc6174cd362389bd1e3848f2b870bdf37837))


### Bug Fixes

* compat with Python 3.14 ([566b7bf](https://github.com/Not-Diamond/not-diamond-python/commit/566b7bf3583a41330dc9ada230e343fc852dd7ad))


### Chores

* **package:** drop Python 3.8 support ([8f6e2eb](https://github.com/Not-Diamond/not-diamond-python/commit/8f6e2eb71d0523fa1d7b6bb39c30ffbbc95363cf))

## 1.0.0-rc10 (2025-11-10)

Full Changelog: [v1.0.0-rc9...v1.0.0-rc10](https://github.com/Not-Diamond/not-diamond-python/compare/v1.0.0-rc9...v1.0.0-rc10)

### Features

* **api:** manual updates ([3b34f4f](https://github.com/Not-Diamond/not-diamond-python/commit/3b34f4fb9f5ed2281a5672179f759f7eccb41dc0))

## 1.0.0-rc9 (2025-11-10)

Full Changelog: [v1.0.0-rc8...v1.0.0-rc9](https://github.com/Not-Diamond/not-diamond-python/compare/v1.0.0-rc8...v1.0.0-rc9)

### Features

* **api:** manual updates ([50911a0](https://github.com/Not-Diamond/not-diamond-python/commit/50911a023f29a7017ec810e55ee55209c5dbdacc))

## 1.0.0-rc8 (2025-11-10)

Full Changelog: [v1.0.0-rc7...v1.0.0-rc8](https://github.com/Not-Diamond/not-diamond-python/compare/v1.0.0-rc7...v1.0.0-rc8)

### Features

* **api:** manual updates ([1d846ce](https://github.com/Not-Diamond/not-diamond-python/commit/1d846ce29e4e8688e82bd64d500d3752af77d6de))

## 1.0.0-rc7 (2025-11-07)

Full Changelog: [v1.0.0-rc6...v1.0.0-rc7](https://github.com/Not-Diamond/not-diamond-python/compare/v1.0.0-rc6...v1.0.0-rc7)

### Features

* **api:** api update ([bdb1ebe](https://github.com/Not-Diamond/not-diamond-python/commit/bdb1ebe855fe24f1c9d93804fea1ef38ae77341d))

## 1.0.0-rc6 (2025-11-06)

Full Changelog: [v1.0.0-rc5...v1.0.0-rc6](https://github.com/Not-Diamond/not-diamond-python/compare/v1.0.0-rc5...v1.0.0-rc6)

### Features

* **api:** manual updates ([e864113](https://github.com/Not-Diamond/not-diamond-python/commit/e864113c227997b0c04a02cad05b8963fe5a9283))

## 1.0.0-rc5 (2025-11-05)

Full Changelog: [v1.0.0-rc4...v1.0.0-rc5](https://github.com/Not-Diamond/not-diamond-python/compare/v1.0.0-rc4...v1.0.0-rc5)

### Features

* **api:** manual updates ([0a7ac49](https://github.com/Not-Diamond/not-diamond-python/commit/0a7ac4986879837b1b93bb31c5b7e6d211a55077))


### Chores

* update SDK settings ([227346c](https://github.com/Not-Diamond/not-diamond-python/commit/227346c8e801e2ee7f0f7c376fb55e5aea606232))

## 1.0.0-rc4 (2025-11-05)

Full Changelog: [v1.0.0-rc3...v1.0.0-rc4](https://github.com/Not-Diamond/not-diamond-python/compare/v1.0.0-rc3...v1.0.0-rc4)

### Features

* **api:** manual updates ([dd9657d](https://github.com/Not-Diamond/not-diamond-python/commit/dd9657df2226d7d46cf99ee8b23eced653155c74))

## 1.0.0-rc3 (2025-11-05)

Full Changelog: [v1.0.0-rc2...v1.0.0-rc3](https://github.com/Not-Diamond/not-diamond-python/compare/v1.0.0-rc2...v1.0.0-rc3)

### Features

* **api:** api update ([0cdedc2](https://github.com/Not-Diamond/not-diamond-python/commit/0cdedc27ef1bab63e433bdc0717c36cc48d60b55))
* **api:** api update ([f717b91](https://github.com/Not-Diamond/not-diamond-python/commit/f717b91a37cd48a63e9ef9458cef6dd899383f2c))
* **api:** api update ([24340ab](https://github.com/Not-Diamond/not-diamond-python/commit/24340ab121937a85e9c4bbc8b644c62b15f75d89))
* **api:** enable tests ([64ccd03](https://github.com/Not-Diamond/not-diamond-python/commit/64ccd03281ae7b420b44cf64910568e3657f24db))
* **api:** regen docs ([c80dbe1](https://github.com/Not-Diamond/not-diamond-python/commit/c80dbe1994cd73b549995b5e91ac86a62a77f5b7))
* **api:** verify mock tests enabled ([638d79b](https://github.com/Not-Diamond/not-diamond-python/commit/638d79bdd90097d9823d02e3dac8b12ab2849d03))


### Chores

* **internal:** grammar fix (it's -&gt; its) ([6d37a12](https://github.com/Not-Diamond/not-diamond-python/commit/6d37a125457223046183bcc8ee7159ed96b80424))
* update SDK settings ([ba3968b](https://github.com/Not-Diamond/not-diamond-python/commit/ba3968b9ef7b2ec9e7b1b3983a6e2a8b31ccbc37))

## 1.0.0-rc2 (2025-10-31)

Full Changelog: [v1.0.0-rc1...v1.0.0-rc2](https://github.com/Not-Diamond/not-diamond-python/compare/v1.0.0-rc1...v1.0.0-rc2)

### Features

* **api:** api update ([f4f83bd](https://github.com/Not-Diamond/not-diamond-python/commit/f4f83bd926d4296f883f5db75de90a5db275867a))

## 1.0.0-rc1 (2025-10-31)

Full Changelog: [v0.3.0...v1.0.0-rc1](https://github.com/Not-Diamond/not-diamond-python/compare/v0.3.0...v1.0.0-rc1)

### Features

* **api:** fix modelSelect error ([eb29990](https://github.com/Not-Diamond/not-diamond-python/commit/eb29990fab14468f39368f7f5b0e4ebf019d0841))
* **api:** manual updates ([b905d72](https://github.com/Not-Diamond/not-diamond-python/commit/b905d72ebec4d42373de62865a85f62d4a87c477))
* **api:** manual updates ([d664d8d](https://github.com/Not-Diamond/not-diamond-python/commit/d664d8d20ab802a9aa0150519a3900d386f7b1d9))


### Bug Fixes

* **client:** close streams without requiring full consumption ([c9f7310](https://github.com/Not-Diamond/not-diamond-python/commit/c9f73103e1747f06da439c77b7d5e322c4d09a4e))


### Chores

* **internal/tests:** avoid race condition with implicit client cleanup ([14e720b](https://github.com/Not-Diamond/not-diamond-python/commit/14e720b4d735b9a52d634b1ec24db5bff9c3aa24))
* update SDK settings ([26ae314](https://github.com/Not-Diamond/not-diamond-python/commit/26ae3141eaa1df28dd8b1d1e5d322fb135bee6b9))

## 0.3.0 (2025-10-24)

Full Changelog: [v0.2.0...v0.3.0](https://github.com/Not-Diamond/not-diamond-python/compare/v0.2.0...v0.3.0)

### Features

* **api:** api update ([d403264](https://github.com/Not-Diamond/not-diamond-python/commit/d4032647605736f1c51d04023d3adb24f448737f))
* **api:** api update ([c7a1198](https://github.com/Not-Diamond/not-diamond-python/commit/c7a1198c1432e833b740f92df9996379f941228f))
* **api:** api update ([9265a0a](https://github.com/Not-Diamond/not-diamond-python/commit/9265a0a3959818b06f157726e68d3c73f7f5d9c9))
* **api:** api update ([880c195](https://github.com/Not-Diamond/not-diamond-python/commit/880c195dc41ac5e500cae9b9a71b0840f97e7556))
* **api:** exclude non sdk endpoints ([fb04bc4](https://github.com/Not-Diamond/not-diamond-python/commit/fb04bc460d7f9f7f191cffcb56868d09fa45edc1))
* **api:** fix missing endpoint ([427d1d3](https://github.com/Not-Diamond/not-diamond-python/commit/427d1d3bdd7be290e66897aa35daba984931e4a4))
* **api:** manual updates ([603c1b7](https://github.com/Not-Diamond/not-diamond-python/commit/603c1b74c64850e1fd8a89e08b1d66d0665188e0))
* **api:** manual updates ([42fb39e](https://github.com/Not-Diamond/not-diamond-python/commit/42fb39e0978aa329f4b5171ff54aaab257558135))
* **api:** report group ([4312188](https://github.com/Not-Diamond/not-diamond-python/commit/43121880104978fa2b88a3ad0e85070a2b322787))


### Chores

* bump `httpx-aiohttp` version to 0.1.9 ([37d5de2](https://github.com/Not-Diamond/not-diamond-python/commit/37d5de2162ece6024539d9e546dd2679ba5e1882))
* **internal:** detect missing future annotations with ruff ([316a749](https://github.com/Not-Diamond/not-diamond-python/commit/316a7493d166e631eafcc888d377dbe340178b24))

## 0.2.0 (2025-10-09)

Full Changelog: [v0.1.0...v0.2.0](https://github.com/Not-Diamond/not-diamond-python/compare/v0.1.0...v0.2.0)

### Features

* **api:** manual updates ([9ee8b3e](https://github.com/Not-Diamond/not-diamond-python/commit/9ee8b3e1220e45b00ce9c9078ab7f54bb1e34e19))

## 0.1.0 (2025-10-09)

Full Changelog: [v0.0.1...v0.1.0](https://github.com/Not-Diamond/not-diamond-python/compare/v0.0.1...v0.1.0)

### Features

* **api:** manual updates ([8062369](https://github.com/Not-Diamond/not-diamond-python/commit/80623692c7da0db7c57b7953af3ec9fdc1e0fca2))


### Chores

* update SDK settings ([ecc0dc6](https://github.com/Not-Diamond/not-diamond-python/commit/ecc0dc63a8d98e9d2178f04cebde730257bae353))
