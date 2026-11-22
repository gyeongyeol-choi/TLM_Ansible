# TLM_Ansible

**TLM_Ansible**은 **TmaxLinux Master**의 소프트웨어 프로비저닝(환경 설정 및 패키지 배포) 기능을 수행하기 위해 구성된 **Ansible Playbook 및 Role 저장소**입니다.  
Agentless 방식의 Ansible을 활용하여 원격 관리 노드의 패키지 관리, 호스트·포트 설정, 미들웨어/DB 배포를 자동화합니다.

---

## 주요 구성 및 기능

### 1. 패키지 관리 (`playbook/pkg/`)
원격 노드의 패키지 상태를 조회하고 설치·업그레이드·삭제를 수행합니다.
* **조회**: `get_list_ins.yml` (설치된 패키지), `get_list_rep.yml` / `get_list_rep2.yml` (저장소 패키지), `get_list_upg.yml` (업그레이드 가능 패키지), `get_pkg_desc.yml` (패키지 상세 정보)
* **배포/제거**: `install_pkg.yml` / `install_pkg2.yml`, `upgrade_pkg.yml` / `upgrade_pkg2.yml`, `delete_pkg.yml` / `delete_pkg2.yml`

### 2. 호스트 및 포트 제어 (`playbook/host/`, `playbook/port/`)
* **호스트 관리**: `passwd_change.yml` (원격 호스트 비밀번호 변경 스크립트 실행 및 정리)
* **포트 관리**: `port_add.yml`, `port_change.yml`, `port_del.yml`

### 3. 미들웨어 · DB Role 및 플레이북 (`roles/`, 루트 `*.yml`)
일반 Linux 및 ProLinux 7 환경용 Role과 실행 플레이북을 제공합니다.
* **Web / WAS**: `apache`, `apache_prolinux7`, `nginx`, `nginx_prolinux7`, `tomcat`
* **Database**: `mysql`, `mysql_prolinux7`, `postgresql`, `postgresql_prolinux7`
* **사내 제품 및 테스트 (`playbook/test/`)**: `jeus.yml`, `tibero.yml`, `webtob.yml` 등

---

## 저장소 구조

```text
.
├── playbook/
│   ├── pkg/         # 패키지 조회·설치·업그레이드·삭제 플레이북
│   ├── host/        # 호스트 제어 플레이북
│   ├── port/        # 방화벽/포트 제어 플레이북
│   └── test/        # JEUS, Tibero, WebtoB 등 테스트 플레이북
├── roles/           # Apache, Nginx, MySQL, PostgreSQL, Tomcat Role
├── vars/
│   └── common_vars.yml  # 공통 변수 (PATH_SC_PKG_LIST, GROUP_NAME 등)
├── files/           # 패키지 목록 JSON 및 실행 파라미터 샘플
├── *.yml            # 서비스별 루트 실행 플레이북 (mysql, nginx, tomcat 등)
└── sc.py            # 패키지 조회/설치/삭제/업그레이드 CLI 래퍼 스크립트
```

---

## 실행 시 참고 사항

* `roles/mysql/defaults/main.yml` 및 `roles/mysql_prolinux7/defaults/main.yml`에는 보안상 `mysql_user_password`, `mysql_root_password` 기본값이 포함되어 있지 않습니다.
* MySQL 플레이북(`mysql.yml`, `mysql_prolinux7.yml`) 실행 시 `--extra-vars`, `group_vars`, 또는 Ansible Vault를 통해 해당 변수를 반드시 전달해 주세요.
  ```bash
  ansible-playbook mysql_prolinux7.yml --extra-vars "mysql_root_password=<password> mysql_user_password=<password>"
  ```
