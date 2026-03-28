# GitHub Push Guide for Zaman Optics Theme

## Prerequisites
- ✅ Git CLI installed and working
- ✅ GitHub account created
- ✅ Git repository initialized in c:\Users\lenovo\Desktop\Zaman-Optics
- ✅ .gitignore file created

## Step-by-Step Commands

### Step 1: Configure Git (First Time Only)
Run these commands once to set up your Git identity:

```powershell
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

Replace "Your Name" and "your.email@example.com" with your actual GitHub username and email.

**Verify it worked:**
```powershell
git config --global user.name
git config --global user.email
```

---

### Step 2: Add All Files to Git
```powershell
git add .
```

This stages all files (except those in .gitignore) for the initial commit.

**Verify files are staged:**
```powershell
git status
```

You should see green "new file:" entries for all files.

---

### Step 3: Create Initial Commit
```powershell
git commit -m "Initial commit: Zaman Optics theme with CSS brand system, hero section enhancement, and product page modes"
```

Or a shorter message:
```powershell
git commit -m "Initial commit: Zaman Optics Shopify theme v1.0"
```

**Verify commit:**
```powershell
git log --oneline
```

Should show your new commit.

---

### Step 4: Create GitHub Repository

You need to create a new repository on GitHub.com:

1. **Go to:** https://github.com/new
2. **Fill in:**
   - Repository name: `zaman-optics-theme`
   - Description: `Premium Shopify Dawn theme with prescription form and brand design system`
   - Visibility: **Public** (for easier Shopify import) or **Private** (more secure)
3. **Don't check:** "Initialize this repository with a README" (you already have one)
4. **Click:** "Create repository"

GitHub will show you the commands to run next.

---

### Step 5: Add Remote Repository and Push

After creating the repository on GitHub, you'll see a screen with commands. Run these:

**First, add the remote:**
```powershell
git remote add origin https://github.com/YOUR_USERNAME/zaman-optics-theme.git
```

Replace `YOUR_USERNAME` with your actual GitHub username.

**Verify remote is set:**
```powershell
git remote -v
```

Should show:
```
origin  https://github.com/YOUR_USERNAME/zaman-optics-theme.git (fetch)
origin  https://github.com/YOUR_USERNAME/zaman-optics-theme.git (push)
```

**Then, push to GitHub:**
```powershell
git branch -M main
git push -u origin main
```

This:
- Renames `master` branch to `main` (GitHub standard)
- Pushes your commits to GitHub
- Sets `main` as the tracking branch

**Verify push succeeded:**
```powershell
git status
```

Should show:
```
On branch main
Your branch is up to date with 'origin/main'.
nothing to commit, working tree clean
```

---

## Alternative: Using SSH (More Secure)

If you prefer SSH instead of HTTPS:

1. **Generate SSH key:**
```powershell
ssh-keygen -t ed25519 -C "your.email@example.com"
```

Press Enter for all prompts to accept defaults.

2. **Add to GitHub:**
   - Go to GitHub Settings > SSH and GPG keys
   - Click "New SSH key"
   - Copy output of: `cat ~/.ssh/id_ed25519.pub`
   - Paste into GitHub form

3. **Use SSH remote:**
```powershell
git remote add origin git@github.com:YOUR_USERNAME/zaman-optics-theme.git
```

Rest of the steps are the same.

---

## Quick Reference: All Commands in Order

```powershell
# Configure Git (first time only)
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"

# Stage all files
git add .

# Verify files
git status

# Create initial commit
git commit -m "Initial commit: Zaman Optics Shopify theme v1.0"

# Verify commit
git log --oneline

# Add GitHub remote (after creating repo on GitHub.com)
git remote add origin https://github.com/YOUR_USERNAME/zaman-optics-theme.git

# Verify remote
git remote -v

# Push to GitHub
git branch -M main
git push -u origin main

# Verify push
git status
```

---

## Importing to Shopify

Once pushed to GitHub, you can import the theme:

1. **Go to:** Shopify Admin > Sales Channels > Themes
2. **Click:** "Add theme" > "Upload theme file" OR "Upload from GitHub"
3. **If using GitHub:**
   - Select your repository: `zaman-optics-theme`
   - Select branch: `main`
   - Click "Upload"
4. **Wait:** Shopify processes the theme (usually takes 1-5 minutes)
5. **Once uploaded:** Click "Customize" to edit or "Preview" to test

---

## If You Get a GitHub Authentication Error

**For HTTPS:**
```powershell
# Use GitHub Personal Access Token instead of password
# 1. Create token at: https://github.com/settings/tokens
# 2. When prompted for password, paste the token
# OR configure credential manager:
git credential approve
```

**For SSH:**
- Make sure SSH key is added to GitHub
- Test connection: `ssh -T git@github.com`
- Should show: `Hi YOUR_USERNAME! You've successfully authenticated...`

---

## Common Issues & Fixes

### Issue: "fatal: not a git repository"
**Solution:** Make sure you're in the correct directory:
```powershell
cd "c:\Users\lenovo\Desktop\Zaman-Optics"
pwd  # Verify you're in the right place
```

### Issue: "Please tell me who you are"
**Solution:** Configure Git user:
```powershell
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

### Issue: "Permission denied (publickey)"
**Solution:** Use HTTPS instead of SSH, or add SSH key to GitHub

### Issue: "nothing to commit, working tree clean"
**This is good!** It means everything is committed and pushed.

### Issue: Files not showing in git add
**Solution:** Check `.gitignore` isn't excluding them:
```powershell
git add . -v  # Verbose mode shows what's being added
```

---

## Verification Checklist

After pushing, verify everything is correct:

- [ ] Go to https://github.com/YOUR_USERNAME/zaman-optics-theme
- [ ] See all files are there (sections/, snippets/, assets/, etc.)
- [ ] See README.md displayed on repository home page
- [ ] See your commit message in commit history
- [ ] See `.gitignore` file in repo
- [ ] See all documentation files

---

## Next Steps

1. **Test in Shopify:**
   - Upload theme from GitHub to Shopify
   - Verify prescription form works
   - Test on mobile and desktop

2. **Update in Shopify:**
   - Make changes in Shopify Theme Editor
   - Download updated theme
   - Git add/commit/push changes
   - Keep GitHub as source of truth

3. **Collaboration:**
   - If working with team, use GitHub branches
   - Create feature branches for new work
   - Use pull requests for review

---

## Support

If you get stuck:
1. Check the error message carefully
2. Refer to "Common Issues & Fixes" above
3. Run `git status` to see current state
4. Run `git log --oneline` to see commit history
5. Visit: https://docs.github.com/en/get-started

---

**Ready? Run the commands in order and you'll have your theme on GitHub! 🚀**
