# **Terraform AWS EC2 Free Tier Demo**  

## **Prerequisites**  
1. **Git** ([Download](https://git-scm.com/downloads))  
2. **Terraform** ([Install Guide](https://developer.hashicorp.com/terraform/tutorials/aws-get-started/install-cli))  
3. **AWS Free Tier Account** ([Sign Up](https://aws.amazon.com/free/))  
4. **AWS CLI** (Optional) ([Install Guide](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html))  

---

## **Step-by-Step Setup**  

### **1. Clone the Project**  
```bash
git clone https://github.com/ChandanKolambe/devops-portfolio.git
cd devops-portfolio/terraform-aws-demo
```

---

### **2. Set Up AWS Account**  
#### **A. Create an IAM User (Avoid Root Account!)**  
1. Go to **AWS IAM Console** → **Users** → **Create User**.  
2. Enter a name (e.g., `terraform`).  
3. Select **Attach Policies Directly** → Add `AdministratorAccess`.  
4. Click **Create User**.  

#### **B. Generate Security Credentials**  
1. Under the user’s **Security Credentials** tab, click **Create Access Key**.  
2. Choose **CLI** and acknowledge the warning.  
3. **Download the `.csv` file** (contains `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY`).  

#### **C. Create an SSH Key Pair**  
1. Go to **EC2 Console** → **Key Pairs** → **Create Key Pair**.  
2. Name: `my-key-pair` → Type: `RSA` → Format: `.pem` (Linux/Mac) or `.ppk` (Windows).  
3. Click **Create Key Pair** (auto-downloads the private key).  
4. Move the key to `~/.ssh/` (Linux/Mac) or `C:\Users\YourUser\.ssh\` (Windows).
---

### **3. Configure AWS Credentials**  
#### **Option A: Use AWS CLI (Recommended)**  
1. Install AWS CLI:  
   ```bash
   aws configure
   ```
2. Enter:  
   - `AWS Access Key ID`: From the downloaded `.csv`.  
   - `AWS Secret Access Key`: From the `.csv`.  
   - `Default Region`: `us-east-1` (Free Tier-friendly).  
   - `Default Output Format`: `json`.  

#### **Option B: Hardcode in `providers.tf` (For Testing Only)**  
```hcl
provider "aws" {
  region     = "us-east-1"
  access_key = "YOUR_ACCESS_KEY"   # Replace with your key
  secret_key = "YOUR_SECRET_KEY"   # ⚠️ Never commit this to Git!
}
```

---

### **4. Initialize Terraform**  
```bash
terraform init
```

---

### **5. Deploy the EC2 Instance**  
```bash
terraform plan
terraform apply  # Type "yes" to confirm
```

---

### **6. Destroy Resources (Avoid Costs!)**  
```bash
terraform destroy
```

---