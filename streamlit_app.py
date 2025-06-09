import streamlit as st
import os
import time
from datetime import datetime
import pandas as pd
from pathlib import Path

from document_processor import DocumentProcessor
from file_watcher import watcher

# Page configuration
st.set_page_config(
    page_title="CricBattle Document Manager",
    page_icon="🏏",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 2rem;
        font-weight: 700;
    }
    .section-header {
        font-size: 1.5rem;
        color: #2e8b57;
        border-bottom: 2px solid #2e8b57;
        padding-bottom: 0.5rem;
        margin: 1.5rem 0 1rem 0;
    }
    .info-box {
        background-color: #f0f8ff;
        padding: 1rem;
        border-radius: 10px;
        border-left: 4px solid #1f77b4;
        margin: 1rem 0;
    }
    .success-box {
        background-color: #f0fff0;
        padding: 1rem;
        border-radius: 10px;
        border-left: 4px solid #32cd32;
        margin: 1rem 0;
    }
    .error-box {
        background-color: #fff0f0;
        padding: 1rem;
        border-radius: 10px;
        border-left: 4px solid #ff6b6b;
        margin: 1rem 0;
    }
    .metric-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1rem;
        border-radius: 10px;
        color: white;
        text-align: center;
        margin: 0.5rem 0;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'processor' not in st.session_state:
    st.session_state.processor = DocumentProcessor()

def main():
    # Header
    st.markdown('<h1 class="main-header">🏏 CricBattle Document Manager</h1>', unsafe_allow_html=True)
    
    # Sidebar
    with st.sidebar:
        st.markdown("### 🛠️ Control Panel")
        
        # Auto-watch toggle
        auto_watch = st.toggle("🔍 Auto-watch Documentation folder", value=watcher.is_active())
        
        if auto_watch and not watcher.is_active():
            watcher.start_watching()
            st.success("✅ Auto-watch enabled")
        elif not auto_watch and watcher.is_active():
            watcher.stop_watching()
            st.info("⏸️ Auto-watch disabled")
        
        st.markdown("---")
        
        # Manual scan button
        if st.button("🔄 Scan for New Documents", type="primary"):
            st.session_state.manual_scan = True
        
        # Documentation folder status
        doc_folder = "Documentation"
        if os.path.exists(doc_folder):
            md_files = list(Path(doc_folder).glob("**/*.md"))
            st.metric("📁 Total MD Files", len(md_files))
        else:
            st.warning("Documentation folder not found")
    
    # Main content tabs
    tab1, tab2, tab3, tab4 = st.tabs(["📊 Dashboard", "📝 Add Document", "🔍 Process Documents", "📋 File Manager"])
    
    with tab1:
        show_dashboard()
    
    with tab2:
        show_add_document()
    
    with tab3:
        show_process_documents()
    
    with tab4:
        show_file_manager()

def show_dashboard():
    st.markdown('<div class="section-header">📊 System Overview</div>', unsafe_allow_html=True)
    
    # Metrics row
    col1, col2, col3, col4 = st.columns(4)
    
    processed_files = st.session_state.processor.get_processed_files_info()
    doc_folder = "Documentation"
    
    with col1:
        total_processed = len(processed_files)
        st.markdown(f'''
        <div class="metric-card">
            <h3>📚 Processed Files</h3>
            <h2>{total_processed}</h2>
        </div>
        ''', unsafe_allow_html=True)
    
    with col2:
        if os.path.exists(doc_folder):
            total_files = len(list(Path(doc_folder).glob("**/*.md")))
        else:
            total_files = 0
        st.markdown(f'''
        <div class="metric-card">
            <h3>📁 Total MD Files</h3>
            <h2>{total_files}</h2>
        </div>
        ''', unsafe_allow_html=True)
    
    with col3:
        status = "🟢 Active" if watcher.is_active() else "🔴 Inactive"
        st.markdown(f'''
        <div class="metric-card">
            <h3>👁️ Auto-watch</h3>
            <h2>{status}</h2>
        </div>
        ''', unsafe_allow_html=True)
    
    with col4:
        try:
            index_stats = st.session_state.processor.pc.Index(st.session_state.processor.index_name).describe_index_stats()
            vector_count = index_stats.total_vector_count
        except:
            vector_count = "N/A"
        
        st.markdown(f'''
        <div class="metric-card">
            <h3>🔢 Vectors in Index</h3>
            <h2>{vector_count}</h2>
        </div>
        ''', unsafe_allow_html=True)
    
    # Recent activity
    if not processed_files.empty:
        st.markdown('<div class="section-header">📈 Recent Files</div>', unsafe_allow_html=True)
        st.dataframe(processed_files, use_container_width=True)
    
    # System status
    st.markdown('<div class="section-header">🔧 System Status</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown('''
        <div class="info-box">
            <h4>🔗 Pinecone Connection</h4>
            <p>✅ Connected to index: <code>chatbot</code></p>
        </div>
        ''', unsafe_allow_html=True)
    
    with col2:
        st.markdown('''
        <div class="info-box">
            <h4>🤖 OpenAI Embeddings</h4>
            <p>✅ Using model: <code>text-embedding-3-small</code></p>
        </div>
        ''', unsafe_allow_html=True)

def show_add_document():
    st.markdown('<div class="section-header">📝 Add New Document</div>', unsafe_allow_html=True)
    
    # File upload section
    st.markdown("### 📤 Upload Markdown File")
    uploaded_file = st.file_uploader(
        "Choose a markdown file",
        type=['md'],
        help="Upload a .md file to add to the documentation"
    )
    
    if uploaded_file is not None:
        # Show file info
        file_details = {
            "Filename": uploaded_file.name,
            "File size": f"{uploaded_file.size / 1024:.2f} KB",
            "File type": uploaded_file.type
        }
        
        col1, col2 = st.columns(2)
        with col1:
            st.json(file_details)
        
        with col2:
            # Preview content
            content = uploaded_file.read().decode('utf-8')
            with st.expander("📄 Preview Content"):
                st.markdown(content[:500] + "..." if len(content) > 500 else content)
        
        # Save file
        if st.button("💾 Save to Documentation Folder", type="primary"):
            doc_folder = "Documentation"
            if not os.path.exists(doc_folder):
                os.makedirs(doc_folder)
            
            file_path = os.path.join(doc_folder, uploaded_file.name)
            
            # Reset file pointer and save
            uploaded_file.seek(0)
            with open(file_path, "wb") as f:
                f.write(uploaded_file.read())
            
            st.success(f"✅ File saved to {file_path}")
            
            # Auto-process if auto-watch is disabled
            if not watcher.is_active():
                with st.spinner("Processing document..."):
                    success = st.session_state.processor.process_single_file(file_path)
                    if success:
                        st.success("✅ Document processed and added to vector store!")
                    else:
                        st.error("❌ Error processing document")
    
    # Manual text input section
    st.markdown("### ✍️ Create New Document")
    
    with st.form("new_document_form"):
        filename = st.text_input("📝 Filename (without .md extension)", placeholder="e.g., new_feature_guide")
        content = st.text_area("📄 Markdown Content", height=300, placeholder="Enter your markdown content here...")
        
        if st.form_submit_button("💾 Create Document", type="primary"):
            if filename and content:
                doc_folder = "Documentation"
                if not os.path.exists(doc_folder):
                    os.makedirs(doc_folder)
                
                file_path = os.path.join(doc_folder, f"{filename}.md")
                
                # Check if file already exists
                if os.path.exists(file_path):
                    st.error(f"❌ File {filename}.md already exists!")
                else:
                    with open(file_path, "w", encoding="utf-8") as f:
                        f.write(content)
                    
                    st.success(f"✅ Document created: {file_path}")
                    
                    # Auto-process if auto-watch is disabled
                    if not watcher.is_active():
                        with st.spinner("Processing document..."):
                            success = st.session_state.processor.process_single_file(file_path)
                            if success:
                                st.success("✅ Document processed and added to vector store!")
                            else:
                                st.error("❌ Error processing document")
            else:
                st.error("❌ Please provide both filename and content")

def show_process_documents():
    st.markdown('<div class="section-header">🔍 Process Documents</div>', unsafe_allow_html=True)
    
    # Manual scan section
    if st.button("🚀 Scan and Process All Documents", type="primary") or st.session_state.get('manual_scan', False):
        if 'manual_scan' in st.session_state:
            del st.session_state.manual_scan
        
        with st.spinner("🔍 Scanning Documentation folder..."):
            results = st.session_state.processor.scan_and_process_new_documents()
        
        # Display results
        col1, col2, col3 = st.columns(3)
        
        with col1:
            if results['processed']:
                st.markdown(f'''
                <div class="success-box">
                    <h4>✅ Processed ({len(results['processed'])})</h4>
                    <ul>
                        {"".join(f"<li>{os.path.basename(f)}</li>" for f in results['processed'])}
                    </ul>
                </div>
                ''', unsafe_allow_html=True)
            else:
                st.info("No new files to process")
        
        with col2:
            if results['skipped']:
                st.markdown(f'''
                <div class="info-box">
                    <h4>⏭️ Skipped ({len(results['skipped'])})</h4>
                    <p>Already up to date</p>
                </div>
                ''', unsafe_allow_html=True)
        
        with col3:
            if results['errors']:
                st.markdown(f'''
                <div class="error-box">
                    <h4>❌ Errors ({len(results['errors'])})</h4>
                    <ul>
                        {"".join(f"<li>{os.path.basename(f)}</li>" for f in results['errors'])}
                    </ul>
                </div>
                ''', unsafe_allow_html=True)
    
    # Processing status
    st.markdown("### 📊 Processing Status")
    
    doc_folder = "Documentation"
    if os.path.exists(doc_folder):
        all_md_files = list(Path(doc_folder).glob("**/*.md"))
        processed_files = st.session_state.processor.processed_files
        
        status_data = []
        for file_path in all_md_files:
            file_path_str = str(file_path)
            is_processed = file_path_str in processed_files
            needs_update = st.session_state.processor._has_file_changed(file_path_str) if is_processed else True
            
            status_data.append({
                "File": file_path.name,
                "Status": "✅ Up to date" if is_processed and not needs_update else "🔄 Needs processing",
                "Last Modified": datetime.fromtimestamp(file_path.stat().st_mtime).strftime("%Y-%m-%d %H:%M:%S"),
                "Size (KB)": f"{file_path.stat().st_size / 1024:.2f}"
            })
        
        if status_data:
            df = pd.DataFrame(status_data)
            st.dataframe(df, use_container_width=True)
        else:
            st.info("No markdown files found in Documentation folder")
    else:
        st.warning("Documentation folder not found")

def show_file_manager():
    st.markdown('<div class="section-header">📋 File Manager</div>', unsafe_allow_html=True)
    
    doc_folder = "Documentation"
    
    if not os.path.exists(doc_folder):
        st.warning("Documentation folder not found")
        return
    
    # File browser
    md_files = list(Path(doc_folder).glob("**/*.md"))
    
    if not md_files:
        st.info("No markdown files found in Documentation folder")
        return
    
    # File selection
    selected_file = st.selectbox("📁 Select a file to manage:", [str(f) for f in md_files])
    
    if selected_file:
        file_path = Path(selected_file)
        
        # File information
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("### 📊 File Information")
            stat = file_path.stat()
            file_info = {
                "Name": file_path.name,
                "Size": f"{stat.st_size / 1024:.2f} KB",
                "Modified": datetime.fromtimestamp(stat.st_mtime).strftime("%Y-%m-%d %H:%M:%S"),
                "Created": datetime.fromtimestamp(stat.st_ctime).strftime("%Y-%m-%d %H:%M:%S")
            }
            st.json(file_info)
        
        with col2:
            st.markdown("### 🛠️ Actions")
            
            # Reprocess file
            if st.button("🔄 Reprocess File"):
                with st.spinner("Processing..."):
                    success = st.session_state.processor.process_single_file(str(file_path))
                    if success:
                        st.success("✅ File reprocessed successfully!")
                    else:
                        st.error("❌ Error processing file")
            
            # Delete file
            if st.button("🗑️ Delete File", type="secondary"):
                st.warning("Are you sure you want to delete this file?")
                if st.button("⚠️ Confirm Delete"):
                    try:
                        file_path.unlink()
                        st.success("✅ File deleted successfully!")
                        st.rerun()
                    except Exception as e:
                        st.error(f"❌ Error deleting file: {e}")
        
        # File content preview
        with st.expander("📄 File Content"):
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                st.markdown(content)
            except Exception as e:
                st.error(f"Error reading file: {e}")

if __name__ == "__main__":
    main()
