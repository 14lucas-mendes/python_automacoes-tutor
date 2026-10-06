# Unifica a skill ai-tutor numa unica copia ativa.
#
# Fonte unica: %USERPROFILE%\.config\mimocode\skills\ai-tutor (skill_root do AGENTS.md).
# Toda outra pasta de skills que tenha um ai-tutor proprio (ex.: ~/.claude/skills/ai-tutor,
# clone da versao publica anterior as ondas) e movida para um backup FORA das pastas de
# skills e substituida por uma juncao (junction) que aponta para a fonte unica.
#
# Uso (PowerShell, sem precisar de administrador):
#   .\unificar-skill-ai-tutor.ps1            # so diagnostica, nao altera nada
#   .\unificar-skill-ai-tutor.ps1 -Apply     # aplica
#
# Desfazer: apagar a juncao (Remove-Item <juncao>, que NAO apaga o alvo) e mover a pasta
# de volta a partir de $BackupRoot.

param(
    [switch]$Apply,
    [string]$Canonical = (Join-Path $env:USERPROFILE ".config\mimocode\skills\ai-tutor"),
    [string]$Study = "E:\Lucas\Documents\Faculdade AI\python_automacoes-tutor",
    [string]$BackupRoot = (Join-Path $env:USERPROFILE "skill-backups")
)

$ErrorActionPreference = "Stop"

# Pastas de skills que hosts de agente leem. A fonte unica e excluida abaixo.
$SkillDirs = @(
    (Join-Path $env:USERPROFILE ".claude\skills"),
    (Join-Path $env:USERPROFILE ".cursor\skills"),
    (Join-Path $env:USERPROFILE ".agents\skills"),
    (Join-Path $env:USERPROFILE ".codex\skills")
)

# Hashes registrados em session-log.md (alinhamento de 22/09).
$Registered = [ordered]@{
    "SKILL.md"                              = "97c690e46f31dd1b8001fe9cc38b05ca1702c459ff2998810fac3b34da9efe5d"
    "references\architecture.md"            = "ae74bfa4a7951f1e80c318769b57330c60b32809e4c8a9b88150fc66bcad97d6"
    "references\learning-contract.md"       = "e3c6e689db1d4ba7ede5ff61e9728d0932ab57e1ac6c5c38a11eb67680c691f2"
    "references\state-contract.md"          = "a74e0312256960584a554411cea8e34c4043926b8fcc018658bcbeefd510b3f6"
    "references\delegation-contract.md"     = "cdaaf4390e0965fac3d3a6d86e104bbc9572e30307e9f885b92eb2ee38cadd58"
    "references\output-contract.md"         = "becc886c1602beefe89eac58ebc8c57e10b31073b2d60b24cd53a6fd4f3bb42d"
    "references\diagnostic-contract.md"     = "8d17f429041d3e8c6c186dbc2b269c5ed5e658113eef284ea3d85ed1fe4b241b"
    "references\learner-profile-contract.md"= "76a9555fb1b5d2c481d33d73d03fb5b73e3be49a110fc48313d56a4b1b5f350e"
    "references\learning-strategies.md"     = "bdb34fe3127a7eb5dbb64a63786e89526a540c12b97059a0d31ddc5f0ac853d3"
    "references\programming.md"             = "0d5010b626a4d9a49b10adeb8cbcb700e420e1bebabb8a630851d1bc8a33087b"
    "references\workflows\session.md"       = "328f97d2ec5dd431441bd3ba598ee81420646c3550c5d2eefaea007e45c875a4"
    "references\workflows\diagnostic.md"    = "d992d9d82a529d3a5808393a46243508693b7cc13314d148ed066177d399c52c"
    "references\workflows\profile.md"       = "1c3d4027e94f2a5187a3e163d4438531edd6452834231c5e7dc4aac552390468"
    "scripts\validate_study.py"             = "0f9fe13868fddda311f73a94ed455d2d76ebaadc6cb7c85d6906b9b83c65c420"
    "scripts\migrate_state.py"              = "b93f50c60743a46b04de079281a85d9bca8c1117f4ed660fa8dda72731cc305f"
    "scripts\learner_profile.py"            = "80dedf07ca190e69abb0a50390f1f7ffa9fe85f3b190fd731fd44ea60caab99b"
    "scripts\practice_strategy.py"          = "fedc302b01d66a3efd233019173e669c7844d5fd626ca66c678f85d29a65c12d"
    "scripts\retrieval.py"                  = "f372cd0b801a1f1301fcb1b226b9207bfe57a868b1e40edd959df7e53456f557"
    "scripts\spaced_repetition.py"          = "f1ad87ac518397c740232e3f9fd54891cfd7ad4f64ea84de12be57ad629e8dcc"
    "scripts\representation.py"             = "cc44bc8b38b2cb7e9ace5df6aede1706b83ce01a2a3b8358d16427bfcc27f481"
}

function Test-IsAiTutor([string]$Dir) {
    $skill = Join-Path $Dir "SKILL.md"
    if (-not (Test-Path -LiteralPath $skill)) { return $false }
    $head = Get-Content -LiteralPath $skill -TotalCount 15 -Encoding UTF8
    return [bool]($head | Select-String -Pattern '^name:\s*["'']?ai-tutor["'']?\s*$')
}

function Invoke-Validation([string]$Label) {
    Write-Host "`n== Validacao ($Label) ==" -ForegroundColor Cyan
    Push-Location -LiteralPath $Canonical
    try {
        & python -m scripts.validate_skill $Canonical
        $skillOk = ($LASTEXITCODE -eq 0)
        & python -m scripts.validate_study $Study
        $studyOk = ($LASTEXITCODE -eq 0)
    } finally { Pop-Location }
    Write-Host ("validate_skill: {0} | validate_study: {1}" -f `
        ($(if ($skillOk) { "PASS" } else { "FAIL" })), ($(if ($studyOk) { "PASS" } else { "FAIL" })))
    return ($skillOk -and $studyOk)
}

# 1. Fonte unica existe?
if (-not (Test-IsAiTutor $Canonical)) {
    throw "Fonte unica nao encontrada ou sem SKILL.md 'name: ai-tutor': $Canonical"
}
$canonicalFull = (Resolve-Path -LiteralPath $Canonical).Path
Write-Host "Fonte unica: $canonicalFull" -ForegroundColor Green

# 2. Hashes da fonte unica contra o registro de 22/09.
Write-Host "`n== Hashes da fonte unica x registro de 22/09 ==" -ForegroundColor Cyan
$hashReport = foreach ($rel in $Registered.Keys) {
    $path = Join-Path $canonicalFull $rel
    $now = if (Test-Path -LiteralPath $path) { (Get-FileHash -LiteralPath $path -Algorithm SHA256).Hash.ToLower() } else { "(ausente)" }
    [pscustomobject]@{
        Arquivo = $rel
        Status  = $(if ($now -eq $Registered[$rel]) { "igual" } else { "DIFERENTE" })
        Atual   = $now
    }
}
$hashReport | Format-Table -AutoSize | Out-String -Width 200 | Write-Host
$diff = @($hashReport | Where-Object Status -ne "igual").Count
Write-Host "$diff arquivo(s) diferem do registro. Diferenca nao bloqueia: registrar os hashes atuais no session-log.md."

# 3. Validar a fonte unica ANTES de apontar tudo para ela.
if (-not (Invoke-Validation "antes")) {
    throw "A fonte unica nao passou na validacao. Nada foi alterado."
}

# 4. Inventario de copias concorrentes.
Write-Host "`n== Copias do ai-tutor nas pastas de skills ==" -ForegroundColor Cyan
$todo = @()
foreach ($dir in $SkillDirs) {
    if (-not (Test-Path -LiteralPath $dir)) { continue }
    foreach ($child in Get-ChildItem -LiteralPath $dir -Directory -Force) {
        if (-not (Test-IsAiTutor $child.FullName)) { continue }
        $item = Get-Item -LiteralPath $child.FullName -Force
        $target = if ($item.LinkType) { @($item.Target)[0] } else { $null }
        if ($target -and ((Resolve-Path -LiteralPath $target).Path -eq $canonicalFull)) {
            Write-Host "OK      $($child.FullName) -> juncao para a fonte unica"
            continue
        }
        Write-Host "DUPLICADA $($child.FullName)" -ForegroundColor Yellow
        $todo += $child.FullName
    }
}
# Garante que o Claude Code tenha a juncao mesmo se nao houver copia nenhuma la.
$claudeLink = Join-Path $env:USERPROFILE ".claude\skills\ai-tutor"
$needClaudeLink = -not (Test-Path -LiteralPath $claudeLink)
if ($needClaudeLink) { Write-Host "AUSENTE $claudeLink (sera criada a juncao)" -ForegroundColor Yellow }

if ($todo.Count -eq 0 -and -not $needClaudeLink) {
    Write-Host "`nJa existe uma unica versao ativa. Nada a fazer." -ForegroundColor Green
    return
}

if (-not $Apply) {
    Write-Host "`nDiagnostico apenas. Rode de novo com -Apply para mover as duplicadas para $BackupRoot e criar as juncoes." -ForegroundColor Yellow
    return
}

# 5. Aplicar: backup fora das pastas de skills + juncao.
$stamp = Get-Date -Format "yyyyMMdd-HHmmss"
New-Item -ItemType Directory -Force -Path $BackupRoot | Out-Null
foreach ($path in $todo) {
    $host_ = Split-Path (Split-Path (Split-Path $path -Parent) -Parent) -Leaf   # ex.: .claude
    $dest = Join-Path $BackupRoot ("{0}-ai-tutor-{1}" -f $host_.TrimStart('.'), $stamp)
    Move-Item -LiteralPath $path -Destination $dest
    Write-Host "Backup:  $path -> $dest"
    New-Item -ItemType Junction -Path $path -Target $canonicalFull | Out-Null
    Write-Host "Juncao:  $path -> $canonicalFull"
}
if ($needClaudeLink) {
    New-Item -ItemType Directory -Force -Path (Split-Path $claudeLink -Parent) | Out-Null
    New-Item -ItemType Junction -Path $claudeLink -Target $canonicalFull | Out-Null
    Write-Host "Juncao:  $claudeLink -> $canonicalFull"
}

# 6. Conferir: o SKILL.md visto pela juncao e o da fonte unica sao o mesmo arquivo.
$a = (Get-FileHash -LiteralPath (Join-Path $claudeLink "SKILL.md")).Hash
$b = (Get-FileHash -LiteralPath (Join-Path $canonicalFull "SKILL.md")).Hash
if ($a -ne $b) { throw "Juncao do Claude Code nao aponta para a fonte unica." }
Write-Host "`nClaude Code agora le a fonte unica (SKILL.md SHA-256 $($b.ToLower()))." -ForegroundColor Green

if (-not (Invoke-Validation "depois")) { throw "Validacao falhou depois da unificacao." }
Write-Host "`nPronto. Reinicie o Claude Code e o Cursor para recarregarem as skills." -ForegroundColor Green
