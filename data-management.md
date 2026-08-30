# :material-database-cog: Data Management

Tools and practices for organizing, storing, backing up, and sharing research data in wildland fire science.

## :material-cloud-upload: Cloud Storage

[:material-microsoft: OneDrive](https://www.microsoft.com/microsoft-365/onedrive){target=_blank} - Microsoft's cloud storage with Office 365 integration. 🆓 5GB free, 💰 1TB with Microsoft 365 subscription.

[:simple-googledrive: Google Drive](https://www.google.com/drive){target=_blank} - Cloud storage with Google Workspace integration. 🆓 15GB free, 💰 100GB+ paid plans.

[:simple-dropbox: Dropbox](https://www.dropbox.com){target=_blank} - Cloud storage with strong sync capabilities and file versioning. 🆓 2GB free, 💰 2TB+ paid plans.

[:simple-box: Box](https://www.box.com){target=_blank} - Enterprise cloud storage with advanced security and compliance features. 💰 Paid plans, free accounts for some educational institutions.

[:simple-nextcloud: Nextcloud](https://nextcloud.com){target=_blank} - Self-hosted open-source cloud storage and collaboration platform. 🆓 Free (self-hosted).

## :material-backup-restore: Backup Solutions

[:material-cloud-sync: Backblaze](https://www.backblaze.com){target=_blank} - Unlimited cloud backup for computers with automatic continuous backup. 💰 $7/mo per computer.

[:material-backup-restore: Arq Backup](https://www.arqbackup.com){target=_blank} - Backup software that stores to your choice of cloud provider (AWS, Google Cloud, etc.). 💰 $50 one-time + cloud storage costs.

[:simple-duplicati: Duplicati](https://www.duplicati.com){target=_blank} - Free open-source backup software supporting multiple cloud storage backends. 🆓 Free.

[:material-harddisk: Time Machine (macOS)](https://support.apple.com/en-us/HT201250){target=_blank} - Built-in macOS backup to external drives. 🆓 Free with macOS.

[:material-content-copy: Acronis Cyber Protect](https://www.acronis.com){target=_blank} - Enterprise backup and recovery with ransomware protection. 💰 Paid plans.

??? Tip "3-2-1 Backup Rule"
    Keep **3** copies of your data, on **2** different types of media, with **1** copy offsite. This protects against hardware failure, disasters, and accidental deletion. Critical research data should always follow this rule.

## :material-file-send: Large File Transfer

[:material-fast-forward: Globus](https://www.globus.org){target=_blank} - High-performance file transfer for research data, optimized for large datasets and institutional repositories. 🆓 Free for researchers.

[:material-upload: WeTransfer](https://wetransfer.com){target=_blank} - Send files up to 2GB free, 200GB with Pro. Simple browser-based transfer. 🆓 Free up to 2GB, 💰 Pro for larger files.

[:material-share: Send Anywhere](https://send-anywhere.com){target=_blank} - Direct device-to-device file transfer without cloud storage. 🆓 Free with limits, 💰 paid plans.

[:simple-dropbox: Dropbox Transfer](https://www.dropbox.com/transfer){target=_blank} - Send up to 2GB free, 100GB with paid plans, files expire after set time. 💰 Paid plans for large files.

[:material-folder-network: Aspera](https://www.ibm.com/products/aspera){target=_blank} - Ultra-fast file transfer for scientific data, used by NASA and other agencies. 💰 Enterprise licensing.

## :material-database-edit: Metadata & Documentation

[:material-image-album: Tropy](https://tropy.org){target=_blank} - Research photo management with metadata organization for field photos and historical documents. 🆓 Free.

[:simple-zotero: Zotero](https://www.zotero.org){target=_blank} - Reference manager with PDF storage and annotation, excellent for research papers. 🆓 Free with 300MB storage, 💰 paid storage plans.

[:simple-mendeley: Mendeley](https://www.mendeley.com){target=_blank} - Reference manager with collaboration features and built-in PDF reader. 🆓 Free with 2GB storage.

[:simple-obsidian: Obsidian](https://obsidian.md){target=_blank} - Local-first markdown note-taking with linking for building personal knowledge bases. 🆓 Free, 💰 optional cloud sync.

[:simple-notion: Notion](https://www.notion.so){target=_blank} - All-in-one workspace for notes, databases, and project management. 🆓 Free personal use, 💰 team plans.

[:material-file-document-outline: README Files](https://www.makeareadme.com){target=_blank} - Best practices for documenting code and data with README files in your repositories.

## :material-shield-check: Data Repositories & Archiving

[:simple-zenodo: Zenodo](https://zenodo.org){target=_blank} - General-purpose open repository for research data, software, and publications with DOI assignment. 🆓 Free, up to 50GB per dataset.

[:simple-figshare: Figshare](https://figshare.com){target=_blank} - Research data repository with visualizations, unlimited public storage. 🆓 Free public storage.

[:material-dna: Dryad](https://datadryad.org){target=_blank} - Curated repository for scientific datasets, often required by journals. 💰 Submission fees apply.

[:simple-osf: Open Science Framework (OSF)](https://osf.io){target=_blank} - Free project management and data sharing for research with DOI minting. 🆓 Free.

[:simple-github: GitHub Releases](https://docs.github.com/en/repositories/releasing-projects-on-github){target=_blank} - Version and archive code with DOI integration via Zenodo. 🆓 Free for public repositories.

[:material-database: Environmental Data Initiative (EDI)](https://environmentaldatainitiative.org){target=_blank} - Repository for ecological and environmental research data. 🆓 Free.

## :material-file-table: Data Organization Best Practices

??? Tip "Folder Structure"
    Use consistent, hierarchical folder structures:
    ```
    ProjectName/
    ├── data/
    │   ├── raw/          # Original, unmodified data
    │   ├── processed/    # Cleaned and processed data
    │   └── metadata/     # Data documentation
    ├── code/             # Analysis scripts
    ├── results/          # Outputs, figures, tables
    ├── documents/        # Papers, reports
    └── README.md         # Project documentation
    ```

??? Tip "File Naming Conventions"
    Use descriptive, consistent file names with dates:
    - Use ISO date format: `YYYYMMDD` or `YYYY-MM-DD`
    - Avoid spaces (use underscores or hyphens): `fire_perimeter_20230615.shp`
    - Include version numbers: `analysis_v02.py`
    - Be descriptive: `modis_burned_area_california_2020.tif`

??? Tip "Version Control"
    Use Git for code and text files. Don't version control large binary files directly; instead use Git LFS or store in data repositories with version tags.

## :material-database-export: Data Formats

### Recommended Open Formats

- **Tabular data**: CSV, Apache Parquet (for large datasets)
- **Geospatial vector**: GeoJSON, GeoPackage (`.gpkg`), Shapefile (`.shp`)
- **Geospatial raster**: GeoTIFF (`.tif`), Cloud Optimized GeoTIFF (COG), NetCDF (`.nc`)
- **Point clouds**: LAS, LAZ (compressed)
- **Documents**: Markdown (`.md`), plain text (`.txt`), PDF/A (archival)
- **Images**: JPEG, PNG, TIFF (uncompressed for archival)

### Avoid Proprietary Formats When Possible

While software like Excel (`.xlsx`) and ArcGIS (`.mxd`, `.lyrx`) are common, save copies in open formats for long-term accessibility and interoperability.

## :material-lock: Data Security & Privacy

??? Tip "Sensitive Data"
    - Never commit passwords, API keys, or credentials to Git repositories
    - Use `.gitignore` to exclude sensitive files
    - Encrypt sensitive data at rest and in transit
    - Follow institutional IRB and data protection policies
    - Check FAIR and CARE data principles for ethical sharing

??? Tip "License Your Data"
    Apply open licenses to your data and code:
    - **Creative Commons (CC BY 4.0)** for data and documents
    - **MIT or Apache 2.0** for code
    - **CC0 (Public Domain)** for maximum openness

    See [Choose a License](https://choosealicense.com){target=_blank} for guidance.

## :material-school: Training Resources

[:material-book-open: FAIR Data Principles](https://www.go-fair.org/fair-principles){target=_blank} - Make data Findable, Accessible, Interoperable, Reusable.

[:material-book-open: CARE Principles](https://www.gida-global.org/care){target=_blank} - Collective Benefit, Authority to Control, Responsibility, Ethics for Indigenous data.

[:simple-github: Good Enough Practices in Scientific Computing](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1005510){target=_blank} - Practical advice for data management and reproducible research.

[:material-database: Data Management Planning](https://dmptool.org){target=_blank} - Tool for creating data management plans required by funding agencies.
