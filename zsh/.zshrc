eval "$(starship init zsh )"
. /home/inferno/.config/zsh/.zsh_aliases_functions
set -o emacs
setopt HIST_IGNORE_ALL_DUPS  # do not put duplicated command into history list
setopt HIST_SAVE_NO_DUPS  # do not save duplicated command
setopt HIST_REDUCE_BLANKS  # remove unnecessary blanks
setopt INC_APPEND_HISTORY_TIME  # append command to history file immediately after execution
setopt autocd extended_glob nomatch menucomplete prompt_subst
setopt interactive_comments completeinword
autoload -Uz vcs_info
autoload -U colors && colors

stty stop undef		# Disable ctrl-s to freeze terminal.
zle_highlight=('paste:none')

autoload -Uz compinit
zstyle ':completion:*' menu select
# zstyle ':completion::complete:lsof:*' menu yes select
zstyle ':completion:*' matcher-list 'm:{[:lower:][:upper:]}={[:upper:][:lower:]}' 'm:{[:lower:][:upper:]}={[:upper:][:lower:]} l:|=* r:|=*' 'm:{[:lower:][:upper:]}={[:upper:][:lower:]} l:|=* r:|=*' 'm:{[:lower:][:upper:]}={[:upper:][:lower:]} l:|=* r:|=*'
zstyle ':completion:*' list-suffixes zstyle ':completion:*' expand prefix suffix 
zmodload zsh/complist
zmodload zsh/zpty
# compinit
_comp_options+=(globdots)		# Include hidden files.

autoload -U up-line-or-beginning-search
autoload -U down-line-or-beginning-search
zle -N up-line-or-beginning-search
zle -N down-line-or-beginning-search

# Colors
autoload -Uz colors && colors
compinit
# source /home/inferno/Documents/Packages/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh
# source ~/.config/zsh/fast-syntax-highlighting/fast-syntax-highlighting.plugin.zsh
# source ~/.config/zsh/zsh-history-substring-search/zsh-history-substring-search.zsh
# source ~/.config/zsh/fzf_widgets/fzf_widgets.zsh
# source ~/.config/zsh/zsh-vi-mode/zsh-vi-mode.plugin.zsh
# source ~/.config/zsh/zsh-vim/zsh-vim-mode.plugin.zsh
eval "$(zoxide init zsh --cmd cd )"
bindkey '^[k' history-substring-search-up
bindkey '^[j' history-substring-search-down
bindkey '^k' up-line-or-beginning-search
bindkey '^j' down-line-or-beginning-search
# bindkey '\e' vi-cmd-mode
bindkey -M menuselect '^j' vi-down-line-or-history
bindkey -M menuselect '^k' vi-up-line-or-history
bindkey -M menuselect '^h' vi-backward-char
bindkey -M menuselect '^l' vi-forward-char

# export OPENAI_API_KEY="$( gpg -qd $SCRIPTS/secrets/pass/chat_gpd_token.gpg )"
