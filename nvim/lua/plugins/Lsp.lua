return {
    {
        "pmizio/typescript-tools.nvim",
        dependencies = { "nvim-lua/plenary.nvim", "neovim/nvim-lspconfig" },
        opts = {},
        enable = true
    },
    {
        "neovim/nvim-lspconfig",
        dependencies = {
            { "folke/neodev.nvim", opts = {} },
            "hrsh7th/cmp-nvim-lsp"
        },
        event = { "BufReadPre", "BufNewFile" },
        config = function()
            local capabilities = require("cmp_nvim_lsp").default_capabilities()
            -- local util = require "lspconfig.util"
            require("neodev").setup({
                -- add any options here, or leave empty to use the default settings
            })
            local lsp = require("lspconfig")
            local border = {
                { "╭", "FloatBorder" },
                { "─", "FloatBorder" },
                { "╮", "FloatBorder" },
                { "│", "FloatBorder" },
                { "╯", "FloatBorder" },
                { "─", "FloatBorder" },
                { "╰", "FloatBorder" },
                { "│", "FloatBorder" },
            }
            vim.diagnostic.config({
                underline = true,
                virtual_text = {
                    prefix = "", -- Could be '●', '▎', 'x'
                    spacing = 4,
                },
                -- virtual_text = false ,
                update_in_insert = true,
            })
            -- LSP settings
            local on_attach = function(client, bufnr)
                vim.api.nvim_set_option_value("omnifunc", "v:lua.vim.lsp.omnifunc", { buf = bufnr })
                vim.lsp.handlers["textDocument/hover"] = vim.lsp.with(vim.lsp.handlers.hover, {
                    border = border,
                })
                vim.lsp.handlers["textDocument/signatureHelp"] = vim.lsp.with(vim.lsp.handlers.signature_help, {
                    border = border,
                })
            end

            lsp.jsonls.setup {
                on_attach = on_attach,
                capabilities = capabilities,
            }

            lsp.bashls.setup({
                on_attach = on_attach,
                capabilities = capabilities,
            })
            -- lsp.ruff_lsp.setup( {
            --     on_attach = on_attach,
            --     capabilities = capabilities,
            --     } )
            lsp.pylsp.setup {
                on_attach = on_attach,
                capabilities = capabilities,
                settings = {
                    pylsp = {
                        plugins = {
                            pycodestyle = {
                                -- ignore = { "E201", "E202", "E231", "W391" },
                                maxLineLength = 100
                            }
                        }
                    }
                }
            }
            lsp.cmake.setup({
                on_attach = on_attach,
                capabilities = capabilities,
            })
            -- lsp.angularls.setup({
            -- 	on_attach = on_attach,
            -- 	capabilities = capabilities,
            -- })
            lsp.html.setup({
                on_attach = on_attach,
                capabilities = capabilities,
            })
            lsp.cssls.setup({
                on_attach = on_attach,
                capabilities = capabilities,
            })

            lsp.quick_lint_js.setup {

                filetypes = { "javascript", "javascriptreact" },
                on_attach = on_attach,
                capabilities = capabilities,
            }

            lsp.prismals.setup({
                cmd = {
                    "/home/inferno/docs/Packages/prisma-lsp/node_modules/@prisma/language-server/dist/src/bin.js",
                    "--stdio"
                },
                on_attach = on_attach,
                capabilities = capabilities,
                -- cmd = {
                --     "papa",
                --     "john"
                -- }

            })
            lsp.nil_ls.setup {

                on_attach = on_attach,
                capabilities = capabilities,
            }
            require("typescript-tools").setup {
                on_attach = on_attach,
                capabilities = capabilities,
                settings = {
                    -- spawn additional tsserver instance to calculate diagnostics on it
                    separate_diagnostic_server = true,
                    -- "change"|"insert_leave" determine when the client asks the server about diagnostic
                    publish_diagnostic_on = "insert_leave",
                    -- array of strings("fix_all"|"add_missing_imports"|"remove_unused"|
                    -- "remove_unused_imports"|"organize_imports") -- or string "all"
                    -- to include all supported code actions
                    -- specify commands exposed as code_actions
                    expose_as_code_action = {},
                    -- string|nil - specify a custom path to `tsserver.js` file, if this is nil or file under path
                    -- not exists then standard path resolution strategy is applied
                    tsserver_path = nil,
                    -- specify a list of plugins to load by tsserver, e.g., for support `styled-components`
                    -- (see 💅 `styled-components` support section)
                    tsserver_plugins = {},
                    -- this value is passed to: https://nodejs.org/api/cli.html#--max-old-space-sizesize-in-megabytes
                    -- memory limit in megabytes or "auto"(basically no limit)
                    tsserver_max_memory = "auto",
                    -- described below
                    tsserver_format_options = {},
                    tsserver_file_preferences = {},
                    -- mirror of VSCode's `typescript.suggest.completeFunctionCalls`
                    complete_function_calls = false,
                },
            }
            -- require'lspconfig'.clangd.setup{on_attach = on_attach} -- Lsp.clang
            lsp.sqlls.setup {
                on_attach = on_attach,
                capabilities = capabilities,
            }
            lsp.clangd.setup({
                on_attach = on_attach,
                capabilities = capabilities,
            })
            -- lsp.ccls.setup {
            --     on_attach = on_attach,
            --     capabilities = capabilities,
            -- }
            -- lsp.tailwindcss.setup {
            --     on_attach = on_attach,
            --     capabilities = capabilities,
            --     filetypes = {"typescript", "javascriptreact" },
            -- }
            -- LATEX
            lsp.texlab.setup {
                on_attach = on_attach,
                capabilities = capabilities,
            }
            -- -- Lsp.Lua

            local sumneko_binary = "/usr/bin/lua-language-server"

            local runtime_path = vim.split(package.path, ";")
            table.insert(runtime_path, "lua/?.lua")
            table.insert(runtime_path, "lua/?/init.lua")

            lsp.lua_ls.setup({
                filetypes = { "lua" },
                on_attach = on_attach,
                capabilities = capabilities,
                cmd = { sumneko_binary, "-E", "usr/share/lua-language-server/main.lua" },
                settings = {
                    Lua = {
                        runtime = {
                            -- Tell the language server which version of Lua you're using (most likely LuaJIT in the case of Neovim)
                            version = "LuaJIT",
                            -- Setup your lua path
                            -- path = runtime_path,
                        },
                        diagnostics = {
                            -- Get the language server to recognize the `vim` global
                            globals = { "vim" },
                        },
                        -- workspace = {
                        --     -- Make the server aware of Neovim runtime files
                        --     -- library = vim.api.nvim_get_runtime_file("", true),
                        --     library = vim.api.nvim_get_runtime_file("*", true),
                        --     -- library = {
                        --     --     [vim.fn.expand("$VIMRUNTIME/lua")] = true,
                        --     --     [vim.fn.expand("$VIMRUNTIME/lua/vim/lsp")] = true,
                        --     --     [vim.fn.stdpath("config") .. "/lua"] = true,
                        --     -- }
                        -- },
                        format = {
                            enable = true,
                            -- Put format options here
                            defaultConfig = {
                                indent_style = "space",
                                indent_size = "4",
                                quote_style = "double"
                            }
                        },
                        -- Do not send telemetry data containing a randomized but unique identifier
                        telemetry = {
                            enable = false,
                        },

                        hints = { enable = true },
                    },
                },
            })
            vim.api.nvim_create_autocmd("LspAttach", {
                group = vim.api.nvim_create_augroup("UserLspConfig", {}),
                callback = function(ev)
                    -- Buffer local mappings.
                    -- See `:help vim.lsp.*` for documentation on any of the below functions
                    --
                    local diagnostic = vim.diagnostic
                    local lsp_b      = vim.lsp.buf
                    local map        = vim.keymap.set

                    map("n", "[d", diagnostic.goto_prev, { desc = "prev error", buffer = ev.buf })
                    map("n", "]d", diagnostic.goto_next, { desc = "next error", buffer = ev.buf })
                    map("n", "<leader>lD", lsp_b.declaration, { desc = "declaration", buffer = ev.buf })
                    map("n", "<leader>lt", lsp_b.type_definition, { desc = "type definition", buffer = ev.buf })
                    map("n", "<leader>lpa", lsp_b.add_workspace_folder,
                        { desc = "add workspace folder", buffer = ev.buf })
                    map("n", "<leader>lpl", function() print(vim.inspect(lsp_b.list_workspace_folders())) end,
                        { desc = "list workspace folders", buffer = ev.buf })
                    map("n", "<leader>lpr", lsp_b.remove_workspace_folder,
                        { desc = "remove workspace folder", buffer = ev.buf })
                    map("n", "<leader>li", lsp_b.implementation, { desc = "Show implementation", buffer = ev.buf })
                    map("n", "<leader>lh", "<cmd>Ouroboros<cr>", { desc = "Switch header", buffer = ev.buf })
                    map("n", "<leader>cR", lsp_b.rename, { desc = "rename", buffer = ev.buf })
                    map("n", "<leader>ca", lsp_b.code_action, { desc = "code action", buffer = ev.buf })
                    map("v", "<leader>ca", lsp_b.code_action, { desc = "code action", buffer = ev.buf })
                    map("n", "<leader>ce", diagnostic.open_float, { desc = "show line diagnostics", buffer = ev.buf })
                    map("n", "<leader>cs", lsp_b.signature_help, { desc = "signature help", buffer = ev.buf })
                    map("n", "K", lsp_b.hover, { desc = "hover", buffer = ev.buf })
                    map("v", "<space>=", function() lsp_b.format({ async = true }) end,
                        { desc = "formatting", buffer = ev.buf })
                    map("n", "<leader>lI", function() lsp_b.inlay_hint(0) end,
                        { desc = "Toggle inlay hints", buffer = ev.buf }

                    )
                end,
            })
        end
    },

}
