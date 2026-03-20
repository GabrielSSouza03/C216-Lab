
alunos: list[dict] = []
_sequencial_por_curso: dict[str, int] = {}


def gerar_matricula(sigla_curso: str) -> str:
    """Gera matrícula no formato SIGLA + número sequencial (ex.: GES1, GES2)."""
    sigla = sigla_curso.strip().upper()
    if not sigla:
        raise ValueError("Sigla do curso não pode ser vazia.")
    if sigla not in _sequencial_por_curso:
        _sequencial_por_curso[sigla] = 1
    n = _sequencial_por_curso[sigla]
    _sequencial_por_curso[sigla] = n + 1
    return f"{sigla}{n}"


def _indice_por_matricula(matricula: str) -> int | None:
    matricula = matricula.strip().upper()
    for i, aluno in enumerate(alunos):
        if aluno["matricula"] == matricula:
            return i
    return None


def cadastrar_aluno() -> None:
    """Create: lê dados e adiciona um aluno à lista."""
    nome = input("Nome: ").strip()
    if not nome:
        print("Nome inválido.")
        return

    email = input("Email: ").strip()
    if not email or "@" not in email:
        print("Email inválido.")
        return

    curso = input("Curso (sigla, ex.: GES, GEC, GET, GEP): ").strip()
    if not curso:
        print("Curso inválido.")
        return

    try:
        matricula = gerar_matricula(curso)
    except ValueError as e:
        print(e)
        return

    alunos.append(
        {
            "nome": nome,
            "email": email,
            "curso": curso.strip().upper(),
            "matricula": matricula,
        }
    )
    print(f"Aluno cadastrado. Matrícula: {matricula}")


def listar_alunos() -> None:
    """Read: exibe todos os alunos."""
    if not alunos:
        print("Nenhum aluno cadastrado.")
        return
    print("\n--- Alunos ---")
    for a in alunos:
        print(
            f"  {a['matricula']} | {a['nome']} | {a['email']} | {a['curso']}"
        )
    print()


def buscar_aluno() -> None:
    """Read: busca e exibe um aluno pela matrícula."""
    matricula = input("Matrícula: ").strip()
    idx = _indice_por_matricula(matricula)
    if idx is None:
        print("Aluno não encontrado.")
        return
    a = alunos[idx]
    print(
        f"Matrícula: {a['matricula']}\n"
        f"Nome: {a['nome']}\n"
        f"Email: {a['email']}\n"
        f"Curso: {a['curso']}\n"
    )


def atualizar_aluno() -> None:
    """Update: altera dados de um aluno; se o curso mudar, gera nova matrícula."""
    matricula = input("Matrícula do aluno a atualizar: ").strip()
    idx = _indice_por_matricula(matricula)
    if idx is None:
        print("Aluno não encontrado.")
        return

    a = alunos[idx]
    print("(Enter vazio mantém o valor atual)\n")

    novo_nome = input(f"Nome [{a['nome']}]: ").strip()
    if novo_nome:
        a["nome"] = novo_nome

    novo_email = input(f"Email [{a['email']}]: ").strip()
    if novo_email:
        if "@" not in novo_email:
            print("Email inválido; email não alterado.")
        else:
            a["email"] = novo_email

    novo_curso = input(f"Curso [{a['curso']}]: ").strip().upper()
    if novo_curso and novo_curso != a["curso"]:
        try:
            a["matricula"] = gerar_matricula(novo_curso)
            a["curso"] = novo_curso
        except ValueError as e:
            print(e)
            return

    print("Dados atualizados.")
    print(f"Matrícula atual: {a['matricula']}")


def remover_aluno() -> None:
    """Delete: remove um aluno pela matrícula."""
    matricula = input("Matrícula do aluno a remover: ").strip()
    idx = _indice_por_matricula(matricula)
    if idx is None:
        print("Aluno não encontrado.")
        return
    removido = alunos.pop(idx)
    print(f"Removido: {removido['nome']} ({removido['matricula']})")


def exibir_menu() -> None:
    print(
        "\n=== CRUD de Alunos ===\n"
        "1 — Cadastrar aluno\n"
        "2 — Listar alunos\n"
        "3 — Buscar aluno por matrícula\n"
        "4 — Atualizar aluno\n"
        "5 — Remover aluno\n"
        "0 — Sair\n"
    )


def main() -> None:
    while True:
        exibir_menu()
        op = input("Escolha uma opção: ").strip()

        if op == "1":
            cadastrar_aluno()
        elif op == "2":
            listar_alunos()
        elif op == "3":
            buscar_aluno()
        elif op == "4":
            atualizar_aluno()
        elif op == "5":
            remover_aluno()
        elif op == "0":
            print("Até logo.")
            break
        else:
            print("Opção inválida.")


if __name__ == "__main__":
    main()
